# 🚀 Intro a las APIs con Python y ML

¡Hola! 🌟

Bienvenid@ al repositorio del curso **"APIs con Python: de consumir a construir"** 

Aquí aprenderás desde cómo consumir APIs externas hasta cómo construir tu propia API con modelos de Machine Learning.

---

## 📁 Estructura del Proyecto

```
Intro-APIs-Python-ML/
│
├── 1_Consumir_APIs.ipynb       # Clase 1: Consumir APIs externas
├── 2_Training_clasificacion.ipynb  # Clase 2: Entrenar modelo de clasificación
├── 3_Training_PCA.ipynb        # Clase 2: Entrenar modelo de clustering
│
├── API_Prediction/             # Backend: API con FastAPI
│   ├── main.py
│   ├── routers/
│   ├── models/                 # Archivos .pkl
│   └── README.md
│
├── App_gradio/                 # Frontend: Interfaz con Gradio
│   ├── app.py
│   └── README.md
│
└── README.md                   # Este archivo
```

---

## 📚 Contenido por Carpeta

### 📓 Notebooks

| Archivo | Descripción |
|---------|-------------|
| `1_Consumir_APIs.ipynb` | Cómo consumir APIs: INEGI, Banxico, yfinance, Our World in Data, Gemini |
| `2_Training_clasificacion.ipynb` | Entrenamiento de Random Forest para predecir si un cliente contratará |
| `3_Training_PCA.ipynb` | Clustering con K-Means + PCA para segmentación de clientes |

> 💡 **Tip:** Los notebooks tienen un botón de **"Open in Colab"** al inicio. Puedes correrlos directamente en Google Colab sin necesidad de instalar nada.

### 🔧 API_Prediction/

Backend construido con **FastAPI** que expone los modelos entrenados.

| Endpoint | Descripción |
|----------|-------------|
| `GET /docs` | Documentación Swagger |
| `GET /health` | Estado de la API |
| `POST /predict/clasificacion` | ¿Contratará el cliente? |
| `POST /predict/segmento` | ¿A qué segmento pertenece? |

**Ejecución:**
```bash
cd API_Prediction
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### 🖥️ App_gradio/

Frontend con **Gradio** para interactuar visualmente con la API.

**Ejecución:**
```bash
cd App_gradio
pip install gradio requests
python app.py
```

---

## 🛠️ Instalación Rápida

```bash
# 1. Clonar el repo
git clone https://github.com/milioe/Intro-APIs-Python-ML.git
cd Intro-APIs-Python-ML

# 2. Instalar dependencias generales
pip install -r requirements.txt

# 3. Correr la API (en una terminal)
cd API_Prediction
python -m uvicorn main:app --reload

# 4. Correr el frontend (en otra terminal)
cd App_gradio
python app.py
```

---

## 🎯 Flujo del Curso

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  1. Consumir    │     │  2. Entrenar    │     │  3. Construir   │
│     APIs        │ ──► │    Modelos      │ ──► │     API         │
│                 │     │                 │     │                 │
│  INEGI, Banxico │     │  Random Forest  │     │  FastAPI        │
│  yfinance       │     │  K-Means + PCA  │     │  + Gradio       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## 📖 Recursos

### APIs Económicas
- [INEGI API](https://www.inegi.org.mx/servicios/api_indicadores.html)
- [Banxico API](https://www.banxico.org.mx/SieAPIRest/service/v1/)
- [Our World in Data](https://ourworldindata.org/)
- [World Bank](https://data.worldbank.org/)
- [FRED (St. Louis Fed)](https://fred.stlouisfed.org/docs/api/fred/)

### SDKs y Librerías
- [yfinance](https://github.com/ranaroussi/yfinance) - Datos financieros
- [Google Gemini](https://ai.google.dev/) - IA generativa

### Documentación
- [FastAPI](https://fastapi.tiangolo.com/)
- [Gradio](https://gradio.app/)
- [scikit-learn](https://scikit-learn.org/)

---

## ☎️ Contacto

¿Dudas, comentarios o sugerencias?

✉️ **Email:** emilio@milioe.com  
🐙 **GitHub:** [@milioe](https://github.com/milioe)

---

## 🎧 Chill & Code

Mientras creaba los contenidos de este curso escuchaba [![este álbum](https://img.shields.io/badge/Spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white)](https://open.spotify.com/intl-es/album/5o2sEyIX07DbCg86qRWOOC?si=6Gdre0prRIWD_JHAEPWDpA)

---

## 📝 Licencia

Este proyecto es de uso educativo. Siéntete libre de usarlo, modificarlo y compartirlo.
