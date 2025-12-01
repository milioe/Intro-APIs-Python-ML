"""
Utilidades para la API de Predicción.
Carga de modelos y funciones de preprocesamiento.
"""

import pickle
import warnings
from pathlib import Path
from typing import Any, Dict

import pandas as pd

# Suprimir warnings de versión de sklearn
warnings.filterwarnings("ignore", category=UserWarning)

# Ruta a los modelos
MODELS_PATH = Path(__file__).parent / "models"

# Descripciones de los segmentos
SEGMENT_DESCRIPTIONS = {
    0: "Clientes contactados previamente que ya conocen los productos del banco",
    1: "Clientes nuevos con recursos financieros limitados",
    2: "Clientes jóvenes, probablemente iniciando su carrera profesional",
    3: "Clientes mayores con mayor patrimonio acumulado"
}


# =============================================================================
# CARGA DE MODELOS
# =============================================================================

def load_pickle(filename: str) -> Any:
    """Carga un archivo pickle desde la carpeta models."""
    filepath = MODELS_PATH / filename
    if not filepath.exists():
        raise FileNotFoundError(f"No se encontró: {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)


def load_clasificacion_models() -> Dict[str, Any]:
    """Carga todos los modelos necesarios para clasificación."""
    return {
        "modelo": load_pickle("clasificacion_modelo_banco.pkl"),
        "scaler": load_pickle("clasificacion_scaler_banco.pkl"),
        "encoders": load_pickle("clasificacion_encoders_banco.pkl"),
        "features": load_pickle("clasificacion_features_banco.pkl"),
    }


def load_segmentacion_models() -> Dict[str, Any]:
    """Carga todos los modelos necesarios para segmentación."""
    return {
        "kmeans": load_pickle("cluster_kmeans_pca_banco.pkl"),
        "pca": load_pickle("cluster_pca_banco.pkl"),
        "scaler": load_pickle("cluster_scaler_segmentacion.pkl"),
        "encoders": load_pickle("cluster_encoders_segmentacion.pkl"),
        "features": load_pickle("cluster_features_segmentacion.pkl"),
        "names": load_pickle("cluster_names.pkl"),
    }


# =============================================================================
# PREPROCESAMIENTO
# =============================================================================

def encode_categorical(data: dict, encoders: dict, features: list) -> pd.DataFrame:
    """
    Convierte un diccionario a DataFrame y aplica Label Encoding.
    
    Args:
        data: Diccionario con los datos del cliente
        encoders: Diccionario de LabelEncoders entrenados
        features: Lista de features en el orden correcto
    
    Returns:
        DataFrame listo para predecir
    """
    df = pd.DataFrame([data])
    
    for col, encoder in encoders.items():
        if col in df.columns:
            try:
                if df[col].iloc[0] in encoder.classes_:
                    df[col] = encoder.transform(df[col])
                else:
                    df[col] = 0  # Valor desconocido
            except Exception:
                df[col] = 0
    
    return df[features]

