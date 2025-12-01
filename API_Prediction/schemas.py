"""
Esquemas Pydantic para validación de datos de entrada y salida.
Estos modelos definen qué datos espera recibir y devolver cada endpoint.
"""

from pydantic import BaseModel, Field
from typing import Literal, Optional


# =============================================================================
# ESQUEMAS PARA CLASIFICACIÓN (¿Contratará el depósito?)
# =============================================================================

class ClienteClasificacion(BaseModel):
    """
    Datos del cliente para predecir si contratará un depósito a plazo.
    Incluye información de la llamada actual (duration).
    """
    # Datos demográficos
    age: int = Field(..., ge=18, le=100, description="Edad del cliente")
    job: str = Field(..., description="Tipo de trabajo (admin, technician, services, etc.)")
    marital: str = Field(..., description="Estado civil (married, single, divorced)")
    education: str = Field(..., description="Nivel educativo (primary, secondary, tertiary)")
    
    # Situación financiera
    default: str = Field(..., description="¿Tiene crédito en default? (yes, no)")
    balance: int = Field(..., description="Saldo promedio anual en euros")
    housing: str = Field(..., description="¿Tiene préstamo hipotecario? (yes, no)")
    loan: str = Field(..., description="¿Tiene préstamo personal? (yes, no)")
    
    # Datos de la campaña actual
    day: int = Field(..., ge=1, le=31, description="Día del mes del contacto")
    month: str = Field(..., description="Mes del contacto (jan, feb, mar, etc.)")
    duration: int = Field(..., ge=0, description="Duración de la llamada en segundos")
    campaign: int = Field(..., ge=1, description="Número de contactos en esta campaña")
    
    # Historial de campañas anteriores
    pdays: int = Field(..., description="Días desde último contacto (-1 si nunca)")
    previous: int = Field(..., ge=0, description="Contactos en campañas anteriores")

    class Config:
        json_schema_extra = {
            "example": {
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
        }


class PrediccionClasificacion(BaseModel):
    """Respuesta del modelo de clasificación."""
    contratara: bool = Field(..., description="Predicción: ¿Contratará el depósito?")
    probabilidad: float = Field(..., ge=0, le=1, description="Probabilidad de contratar")
    etiqueta: str = Field(..., description="Etiqueta legible (Sí/No)")


# =============================================================================
# ESQUEMAS PARA SEGMENTACIÓN (¿A qué cluster pertenece?)
# =============================================================================

class ClienteSegmentacion(BaseModel):
    """
    Datos del cliente para asignarlo a un segmento.
    No incluye day ni month (no relevantes para segmentación).
    """
    # Datos demográficos
    age: int = Field(..., ge=18, le=100, description="Edad del cliente")
    job: str = Field(..., description="Tipo de trabajo")
    marital: str = Field(..., description="Estado civil")
    education: str = Field(..., description="Nivel educativo")
    
    # Situación financiera
    default: str = Field(..., description="¿Tiene crédito en default?")
    balance: int = Field(..., description="Saldo promedio anual en euros")
    housing: str = Field(..., description="¿Tiene préstamo hipotecario?")
    loan: str = Field(..., description="¿Tiene préstamo personal?")
    
    # Datos de contacto
    duration: int = Field(..., ge=0, description="Duración de la llamada en segundos")
    campaign: int = Field(..., ge=1, description="Número de contactos en esta campaña")
    pdays: int = Field(..., description="Días desde último contacto (-1 si nunca)")
    previous: int = Field(..., ge=0, description="Contactos en campañas anteriores")

    class Config:
        json_schema_extra = {
            "example": {
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
            }
        }


class PrediccionSegmento(BaseModel):
    """Respuesta del modelo de segmentación."""
    cluster: int = Field(..., ge=0, le=3, description="Número del cluster (0-3)")
    segmento: str = Field(..., description="Nombre del segmento")
    descripcion: str = Field(..., description="Descripción del perfil")


# =============================================================================
# ESQUEMA PARA HEALTH CHECK
# =============================================================================

class HealthResponse(BaseModel):
    """Respuesta del endpoint de salud."""
    status: str
    modelos_cargados: dict
    version: str

