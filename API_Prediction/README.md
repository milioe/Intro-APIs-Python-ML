# 🏦 API de Predicción Bancaria

API REST construida con **FastAPI** que expone dos modelos de Machine Learning entrenados con datos de campañas de marketing bancario.

---

## 📖 Contexto del Proyecto

Este proyecto forma parte del curso **"Intro a APIs con Python y ML"**. El objetivo es demostrar cómo:

1. Entrenar modelos de ML (clasificación y clustering)
2. Exportar los modelos entrenados (`.pkl`)
3. Construir una API que consuma esos modelos
4. Desplegar la API para que otros la consuman

### Dataset

Utilizamos el **Bank Marketing Dataset** de UCI, que contiene información de campañas de telemarketing de un banco portugués. El objetivo original era predecir si un cliente contrataría un depósito a plazo.

**Variables del cliente:**
| Variable | Descripción | Valores |
|----------|-------------|---------|
| `age` | Edad | 18-100 |
| `job` | Ocupación | admin, technician, services, management, retired, blue-collar, unemployed, entrepreneur, housemaid, self-employed, student, unknown |
| `marital` | Estado civil | married, single, divorced |
| `education` | Educación | primary, secondary, tertiary, unknown |
| `default` | ¿Crédito en mora? | yes, no |
| `balance` | Saldo promedio anual (€) | Entero |
| `housing` | ¿Hipoteca? | yes, no |
| `loan` | ¿Préstamo personal? | yes, no |

**Variables de la campaña:**
| Variable | Descripción |
|----------|-------------|
| `day` | Día del mes del contacto (1-31) |
| `month` | Mes del contacto (jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) |
| `duration` | Duración de la llamada en segundos |
| `campaign` | Número de contactos en esta campaña |
| `pdays` | Días desde el último contacto (-1 si nunca) |
| `previous` | Contactos en campañas anteriores |

---

## 🎯 Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/docs` | GET | Documentación interactiva (Swagger UI) |
| `/redoc` | GET | Documentación alternativa (ReDoc) |
| `/health` | GET | Estado de la API y modelos cargados |
| `/predict/clasificacion` | POST | Predice si el cliente contratará |
| `/predict/segmento` | POST | Asigna al cliente a un segmento |

---

## 🧠 Modelos

### 1. Clasificación - Random Forest

**Pregunta:** ¿Este cliente contratará un depósito a plazo?

**Entrenamiento:** Ver `2_Training_clasificacion.ipynb`
- Modelo: Random Forest Classifier
- Preprocesamiento: Label Encoding + MinMax Scaling
- Métricas: Accuracy ~90%, Recall ~85%

**Flujo de predicción:**
```
Input JSON → Label Encoding → Scaling → Random Forest → {contratará, probabilidad}
```

**Ejemplo de respuesta:**
```json
{
  "contratara": true,
  "probabilidad": 0.7342,
  "etiqueta": "Sí contratará"
}
```

> **Nota:** El campo `probabilidad` viene de `predict_proba()`, que retorna la probabilidad de que pertenezca a la clase positiva (sí contrata).

---

### 2. Segmentación - K-Means + PCA

**Pregunta:** ¿A qué segmento de mercado pertenece este cliente?

**Entrenamiento:** Ver `3_Training_PCA.ipynb`
- Modelo: K-Means (k=4) sobre componentes PCA
- Preprocesamiento: Label Encoding + StandardScaler + PCA (3 componentes)

**Flujo de predicción:**
```
Input JSON → Label Encoding → StandardScaler → PCA → K-Means → {cluster, segmento}
```

**Segmentos identificados:**
| Cluster | Nombre | Perfil |
|---------|--------|--------|
| 0 | **Recurrentes** | Clientes ya contactados, conocen los productos |
| 1 | **Nuevos Estándar** | Primera vez contactados, recursos limitados |
| 2 | **Jóvenes Profesionales** | Menor edad, iniciando carrera |
| 3 | **Premium Seniors** | Mayores, alto patrimonio acumulado |

**Ejemplo de respuesta:**
```json
{
  "cluster": 2,
  "segmento": "Jóvenes Profesionales",
  "descripcion": "Clientes jóvenes, probablemente iniciando su carrera profesional"
}
```

---

## 📁 Estructura del Proyecto

```
API_Prediction/
│
├── main.py                 # Configuración de FastAPI, CORS, routers
├── schemas.py              # Modelos Pydantic para validación de entrada/salida
├── utils.py                # Carga de modelos y funciones de preprocesamiento
│
├── routers/
│   ├── __init__.py
│   └── predictions.py      # Endpoints POST /predict/*
│
├── models/                 # Archivos .pkl exportados de los notebooks
│   ├── clasificacion_modelo_banco.pkl      # Random Forest entrenado
│   ├── clasificacion_scaler_banco.pkl      # MinMaxScaler
│   ├── clasificacion_encoders_banco.pkl    # LabelEncoders
│   ├── clasificacion_features_banco.pkl    # Lista de features
│   ├── cluster_kmeans_pca_banco.pkl        # K-Means entrenado
│   ├── cluster_pca_banco.pkl               # PCA entrenado
│   ├── cluster_scaler_segmentacion.pkl     # StandardScaler
│   ├── cluster_encoders_segmentacion.pkl   # LabelEncoders
│   ├── cluster_features_segmentacion.pkl   # Lista de features
│   └── cluster_names.pkl                   # Nombres de clusters
│
├── requirements.txt        # Dependencias
└── README.md               # Esta documentación
```

### ¿Qué hace cada archivo?

| Archivo | Responsabilidad |
|---------|-----------------|
| `main.py` | Inicializa FastAPI, configura CORS, incluye routers, define `/health` |
| `schemas.py` | Define qué datos espera recibir y devolver cada endpoint (validación) |
| `utils.py` | Carga los `.pkl` y tiene la función `encode_categorical()` |
| `routers/predictions.py` | Contiene la lógica de los endpoints `/predict/*` |

---

## 🚀 Ejecución Local

### 1. Instalar dependencias
```bash
cd API_Prediction
pip install -r requirements.txt
```

### 2. Ejecutar servidor
```bash
python -m uvicorn main:app --reload
```

### 3. Abrir documentación
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 🌐 Deploy en Replit

1. Crear nuevo Repl → **Import from GitHub**
2. Subir la carpeta `API_Prediction` completa
3. En el archivo `.replit`, configurar:
   ```
   run = "uvicorn main:app --host 0.0.0.0 --port 8000"
   ```
4. Click en **Run**

---

## 🧪 Ejemplos de Uso

### Con cURL

**Clasificación:**
```bash
curl -X POST "http://localhost:8000/predict/clasificacion" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "job": "management",
    "marital": "married",
    "education": "tertiary",
    "default": "no",
    "balance": 1500,
    "housing": "yes",
    "loan": "no",
    "day": 15,
    "month": "may",
    "duration": 300,
    "campaign": 2,
    "pdays": -1,
    "previous": 0
  }'
```

**Segmentación:**
```bash
curl -X POST "http://localhost:8000/predict/segmento" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "job": "management",
    "marital": "married",
    "education": "tertiary",
    "default": "no",
    "balance": 2000,
    "housing": "yes",
    "loan": "no",
    "duration": 250,
    "campaign": 2,
    "pdays": -1,
    "previous": 0
  }'
```

### Con Python

```python
import requests

# Clasificación
response = requests.post(
    "http://localhost:8000/predict/clasificacion",
    json={
        "age": 35,
        "job": "management",
        "marital": "married",
        "education": "tertiary",
        "default": "no",
        "balance": 1500,
        "housing": "yes",
        "loan": "no",
        "day": 15,
        "month": "may",
        "duration": 300,
        "campaign": 2,
        "pdays": -1,
        "previous": 0
    }
)
print(response.json())
# {'contratara': True, 'probabilidad': 0.73, 'etiqueta': 'Sí contratará'}
```

---

## 📚 Notebooks Relacionados

| Notebook | Descripción |
|----------|-------------|
| `1_Consumir_APIs.ipynb` | Cómo consumir APIs externas (INEGI, Banxico, yfinance, Gemini) |
| `2_Training_clasificacion.ipynb` | Entrenamiento del modelo de clasificación |
| `3_Training_PCA.ipynb` | Entrenamiento del modelo de segmentación |

---

## 🛠️ Tecnologías

- **FastAPI** - Framework web moderno para APIs
- **Pydantic** - Validación de datos
- **scikit-learn** - Modelos de ML
- **pandas** - Manipulación de datos
- **uvicorn** - Servidor ASGI

---

## 👨‍🏫 Desarrollado para

**Curso:** Intro a APIs con Python y ML  
**Objetivo:** Aprender a construir y consumir APIs con modelos de Machine Learning
