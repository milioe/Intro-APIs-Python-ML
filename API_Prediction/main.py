"""
API de Predicción Bancaria
==========================
Punto de entrada principal de la API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.predictions import router as predictions_router, get_models_status
from schemas import HealthResponse

# =============================================================================
# CONFIGURACIÓN DE LA APP
# =============================================================================

app = FastAPI(
    title="🏦 API de Predicción Bancaria",
    description="""
## Endpoints disponibles

### 1. Clasificación (`/predict/clasificacion`)
Predice si un cliente contratará un depósito a plazo.
- **Modelo:** Random Forest

### 2. Segmentación (`/predict/segmento`)  
Asigna a un cliente a un segmento de mercado.
- **Modelo:** K-Means + PCA
- **Segmentos:** Recurrentes, Nuevos Estándar, Jóvenes Profesionales, Premium Seniors

---
Desarrollado para **Intro a APIs con Python y ML**
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# ROUTERS
# =============================================================================

app.include_router(predictions_router)

# =============================================================================
# ENDPOINTS BASE
# =============================================================================

@app.get("/health", response_model=HealthResponse, tags=["Sistema"])
async def health_check():
    """Verifica el estado de la API y los modelos."""
    status = get_models_status()
    return HealthResponse(
        status="ok" if all(status.values()) else "degraded",
        modelos_cargados=status,
        version="1.0.0"
    )


# =============================================================================
# EJECUCIÓN
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
