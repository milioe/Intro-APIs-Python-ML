"""
Router de Predicciones.
Endpoints para clasificación y segmentación.
"""

from fastapi import APIRouter, HTTPException

from schemas import (
    ClienteClasificacion,
    ClienteSegmentacion,
    PrediccionClasificacion,
    PrediccionSegmento,
)
from utils import (
    encode_categorical,
    load_clasificacion_models,
    load_segmentacion_models,
    SEGMENT_DESCRIPTIONS,
)

router = APIRouter(prefix="/predict", tags=["Predicción"])

# Cargar modelos al iniciar
try:
    clf = load_clasificacion_models()
    CLASIFICACION_OK = True
except Exception as e:
    print(f"⚠️ Error cargando clasificación: {e}")
    CLASIFICACION_OK = False
    clf = {}

try:
    seg = load_segmentacion_models()
    SEGMENTACION_OK = True
except Exception as e:
    print(f"⚠️ Error cargando segmentación: {e}")
    SEGMENTACION_OK = False
    seg = {}


@router.post("/clasificacion", response_model=PrediccionClasificacion)
async def predecir_clasificacion(cliente: ClienteClasificacion):
    """
    🎯 Predice si un cliente contratará un depósito a plazo.
    
    **Modelo:** Random Forest
    """
    if not CLASIFICACION_OK:
        raise HTTPException(503, "Modelo de clasificación no disponible")
    
    try:
        # Preprocesar
        df = encode_categorical(
            cliente.model_dump(),
            clf["encoders"],
            clf["features"]
        )
        
        # Escalar y predecir
        X_scaled = clf["scaler"].transform(df)
        prediccion = clf["modelo"].predict(X_scaled)[0]
        probabilidad = clf["modelo"].predict_proba(X_scaled)[0][1]
        
        return PrediccionClasificacion(
            contratara=bool(prediccion),
            probabilidad=round(float(probabilidad), 4),
            etiqueta="Sí contratará" if prediccion else "No contratará"
        )
    
    except Exception as e:
        raise HTTPException(500, f"Error: {str(e)}")


@router.post("/segmento", response_model=PrediccionSegmento)
async def predecir_segmento(cliente: ClienteSegmentacion):
    """
    📊 Asigna un cliente a un segmento de mercado.
    
    **Modelo:** K-Means + PCA
    
    **Segmentos:**
    - Recurrentes
    - Nuevos Estándar
    - Jóvenes Profesionales
    - Premium Seniors
    """
    if not SEGMENTACION_OK:
        raise HTTPException(503, "Modelo de segmentación no disponible")
    
    try:
        # Preprocesar
        df = encode_categorical(
            cliente.model_dump(),
            seg["encoders"],
            seg["features"]
        )
        
        # Escalar → PCA → K-Means
        X_scaled = seg["scaler"].transform(df)
        X_pca = seg["pca"].transform(X_scaled)
        cluster = seg["kmeans"].predict(X_pca)[0]
        
        return PrediccionSegmento(
            cluster=int(cluster),
            segmento=seg["names"][cluster],
            descripcion=SEGMENT_DESCRIPTIONS[cluster]
        )
    
    except Exception as e:
        raise HTTPException(500, f"Error: {str(e)}")


# Exportar estado para health check
def get_models_status() -> dict:
    return {
        "clasificacion": CLASIFICACION_OK,
        "segmentacion": SEGMENTACION_OK
    }

