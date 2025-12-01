"""
Frontend con Gradio para la API de Predicción Bancaria.
Conecta con el backend de FastAPI para hacer predicciones.
"""

import gradio as gr
import requests

# =============================================================================
# FUNCIONES DE PREDICCIÓN
# =============================================================================

def predecir_clasificacion(
    api_url, age, job, marital, education, default, balance,
    housing, loan, day, month, duration, campaign, pdays, previous
):
    """Llama al endpoint de clasificación."""
    try:
        url = f"{api_url.rstrip('/')}/predict/clasificacion"
        payload = {
            "age": int(age),
            "job": job,
            "marital": marital,
            "education": education,
            "default": default,
            "balance": int(balance),
            "housing": housing,
            "loan": loan,
            "day": int(day),
            "month": month,
            "duration": int(duration),
            "campaign": int(campaign),
            "pdays": int(pdays),
            "previous": int(previous)
        }
        response = requests.post(url, json=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            emoji = "✅" if data["contratara"] else "❌"
            return f"""
{emoji} **{data['etiqueta']}**

📊 **Probabilidad:** {data['probabilidad']*100:.1f}%
            """
        else:
            return f"❌ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"


def predecir_segmento(
    api_url, age, job, marital, education, default, balance,
    housing, loan, duration, campaign, pdays, previous
):
    """Llama al endpoint de segmentación."""
    try:
        url = f"{api_url.rstrip('/')}/predict/segmento"
        payload = {
            "age": int(age),
            "job": job,
            "marital": marital,
            "education": education,
            "default": default,
            "balance": int(balance),
            "housing": housing,
            "loan": loan,
            "duration": int(duration),
            "campaign": int(campaign),
            "pdays": int(pdays),
            "previous": int(previous)
        }
        response = requests.post(url, json=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            emojis = {0: "🔄", 1: "💼", 2: "🌱", 3: "💎"}
            emoji = emojis.get(data["cluster"], "📊")
            return f"""
{emoji} **Segmento: {data['segmento']}**

📋 **Cluster:** {data['cluster']}

📝 **Descripción:** {data['descripcion']}
            """
        else:
            return f"❌ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"


# =============================================================================
# OPCIONES DE DROPDOWNS
# =============================================================================

JOBS = ["admin", "technician", "services", "management", "retired", 
        "blue-collar", "unemployed", "entrepreneur", "housemaid", 
        "self-employed", "student", "unknown"]

MARITAL = ["married", "single", "divorced"]

EDUCATION = ["primary", "secondary", "tertiary", "unknown"]

YES_NO = ["yes", "no"]

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", 
          "jul", "aug", "sep", "oct", "nov", "dec"]


# =============================================================================
# INTERFAZ GRADIO
# =============================================================================

with gr.Blocks(title="🏦 Predicción Bancaria", theme=gr.themes.Soft()) as app:
    
    gr.Markdown("""
    # 🏦 API de Predicción Bancaria
    
    Conecta con tu backend de FastAPI para hacer predicciones de:
    - **Clasificación:** ¿El cliente contratará un depósito?
    - **Segmentación:** ¿A qué segmento pertenece?
    """)
    
    # URL del backend
    api_url = gr.Textbox(
        label="🔗 URL del Backend",
        placeholder="http://localhost:8000",
        value="http://localhost:8000"
    )
    
    with gr.Tabs():
        
        # =================================================================
        # TAB 1: CLASIFICACIÓN
        # =================================================================
        with gr.Tab("🎯 Clasificación"):
            gr.Markdown("### ¿El cliente contratará un depósito a plazo?")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("**Datos del cliente**")
                    clf_age = gr.Number(label="Edad", value=35)
                    clf_job = gr.Dropdown(label="Trabajo", choices=JOBS, value="management")
                    clf_marital = gr.Dropdown(label="Estado civil", choices=MARITAL, value="married")
                    clf_education = gr.Dropdown(label="Educación", choices=EDUCATION, value="tertiary")
                    clf_default = gr.Dropdown(label="¿Crédito en mora?", choices=YES_NO, value="no")
                    clf_balance = gr.Number(label="Balance (€)", value=1500)
                    clf_housing = gr.Dropdown(label="¿Hipoteca?", choices=YES_NO, value="yes")
                    clf_loan = gr.Dropdown(label="¿Préstamo personal?", choices=YES_NO, value="no")
                
                with gr.Column():
                    gr.Markdown("**Datos de la campaña**")
                    clf_day = gr.Number(label="Día del mes", value=15, minimum=1, maximum=31)
                    clf_month = gr.Dropdown(label="Mes", choices=MONTHS, value="may")
                    clf_duration = gr.Number(label="Duración llamada (seg)", value=300)
                    clf_campaign = gr.Number(label="Contactos esta campaña", value=2, minimum=1)
                    clf_pdays = gr.Number(label="Días desde último contacto", value=-1)
                    clf_previous = gr.Number(label="Contactos anteriores", value=0)
                    
                    gr.Markdown("---")
                    clf_btn = gr.Button("🚀 Predecir", variant="primary")
                    clf_output = gr.Markdown()
            
            clf_btn.click(
                predecir_clasificacion,
                inputs=[api_url, clf_age, clf_job, clf_marital, clf_education, 
                        clf_default, clf_balance, clf_housing, clf_loan,
                        clf_day, clf_month, clf_duration, clf_campaign, 
                        clf_pdays, clf_previous],
                outputs=clf_output
            )
        
        # =================================================================
        # TAB 2: SEGMENTACIÓN
        # =================================================================
        with gr.Tab("📊 Segmentación"):
            gr.Markdown("### ¿A qué segmento de mercado pertenece?")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("**Datos del cliente**")
                    seg_age = gr.Number(label="Edad", value=35)
                    seg_job = gr.Dropdown(label="Trabajo", choices=JOBS, value="management")
                    seg_marital = gr.Dropdown(label="Estado civil", choices=MARITAL, value="married")
                    seg_education = gr.Dropdown(label="Educación", choices=EDUCATION, value="tertiary")
                    seg_default = gr.Dropdown(label="¿Crédito en mora?", choices=YES_NO, value="no")
                    seg_balance = gr.Number(label="Balance (€)", value=2000)
                
                with gr.Column():
                    gr.Markdown("**Datos de contacto**")
                    seg_housing = gr.Dropdown(label="¿Hipoteca?", choices=YES_NO, value="yes")
                    seg_loan = gr.Dropdown(label="¿Préstamo personal?", choices=YES_NO, value="no")
                    seg_duration = gr.Number(label="Duración llamada (seg)", value=250)
                    seg_campaign = gr.Number(label="Contactos esta campaña", value=2, minimum=1)
                    seg_pdays = gr.Number(label="Días desde último contacto", value=-1)
                    seg_previous = gr.Number(label="Contactos anteriores", value=0)
                    
                    gr.Markdown("---")
                    seg_btn = gr.Button("🚀 Segmentar", variant="primary")
                    seg_output = gr.Markdown()
            
            seg_btn.click(
                predecir_segmento,
                inputs=[api_url, seg_age, seg_job, seg_marital, seg_education,
                        seg_default, seg_balance, seg_housing, seg_loan,
                        seg_duration, seg_campaign, seg_pdays, seg_previous],
                outputs=seg_output
            )
    
    gr.Markdown("""
    ---
    **Segmentos disponibles:**
    - 🔄 **Recurrentes** - Clientes ya contactados
    - 💼 **Nuevos Estándar** - Primera vez, recursos limitados
    - 🌱 **Jóvenes Profesionales** - Menor edad, iniciando carrera
    - 💎 **Premium Seniors** - Mayores, alto patrimonio
    """)


# =============================================================================
# EJECUCIÓN
# =============================================================================

if __name__ == "__main__":
    app.launch()

