# 🖥️ Frontend con Gradio

Interfaz gráfica para interactuar con la API de Predicción Bancaria.

---

## ¿Qué es esto?

Un frontend simple construido con [Gradio](https://gradio.app/) que se conecta al backend de FastAPI (`API_Prediction/`) para hacer predicciones.

**Características:**
- Campo para configurar la URL del backend
- Dos tabs: Clasificación y Segmentación
- Formularios con dropdowns para los valores válidos
- Resultados formateados con emojis

---

## 🚀 Ejecución

### 1. Instalar Gradio
```bash
pip install gradio requests
```

### 2. Asegúrate de tener el backend corriendo
```bash
cd ../API_Prediction
python -m uvicorn main:app --reload
```

### 3. Ejecutar el frontend
```bash
cd App_gradio
python app.py
```

### 4. Abrir en navegador
Gradio abrirá automáticamente `http://localhost:7860`

---

## 📸 Vista previa

```
┌─────────────────────────────────────────┐
│  🏦 API de Predicción Bancaria          │
│                                         │
│  🔗 URL del Backend: [http://localhost] │
│                                         │
│  ┌─────────────┬─────────────┐          │
│  │ 🎯 Clasif.  │ 📊 Segment. │          │
│  └─────────────┴─────────────┘          │
│                                         │
│  Edad: [35]     Trabajo: [management]   │
│  ...                                    │
│                                         │
│  [🚀 Predecir]                          │
│                                         │
│  ✅ Sí contratará                       │
│  📊 Probabilidad: 73.4%                 │
└─────────────────────────────────────────┘
```

---

## 🔗 Conexión con el Backend

Por defecto apunta a `http://localhost:8000`. Si tu backend está en otro lugar (ej: Replit), solo cambia la URL en el campo superior.

**Ejemplos:**
- Local: `http://localhost:8000`
- Replit: `https://tu-repl.usuario.repl.co`

---

## 📁 Estructura

```
App_gradio/
├── app.py      # Aplicación Gradio (todo en un archivo)
└── README.md   # Esta documentación
```

---

## 🛠️ Tecnologías

- **Gradio** - Framework para interfaces ML
- **Requests** - Llamadas HTTP al backend

