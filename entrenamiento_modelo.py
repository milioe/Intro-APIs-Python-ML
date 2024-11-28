import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Configuración de la semilla para reproducibilidad
np.random.seed(42)

# Generar datos ficticios
n = 1000  # Número de observaciones

# Variables independientes
educacion = np.random.randint(5, 21, n)  # Años de educación (5 a 20 años)
experiencia = np.random.randint(0, 30, n)  # Años de experiencia laboral (0 a 30 años)
horas_semana = np.random.randint(20, 60, n)  # Horas trabajadas por semana (20 a 60 horas)

# Generar ingreso con relaciones lineales y algo de ruido
ingreso = (
    1000 +  # Base
    800 * np.log(educacion) +  # Relación logarítmica con educación
    400 * np.sqrt(experiencia) +  # Relación raíz cuadrada con experiencia
    25 * horas_semana +  # Relación lineal con horas trabajadas
    np.random.normal(0, 500, n)  # Ruido normal con desviación estándar de 500
)

# Crear un DataFrame
data = pd.DataFrame({
    "educacion": educacion,
    "experiencia": experiencia,
    "horas_semana": horas_semana,
    "ingreso": ingreso
})

# Dividir en conjunto de entrenamiento y prueba
X = data[["educacion", "experiencia", "horas_semana"]]
y = data["ingreso"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
print(f"Error cuadrático medio: {mean_squared_error(y_test, y_pred)}")

# Guardar el modelo en un archivo pickle
with open("modelo_regresion_lineal.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modelo guardado como 'modelo_regresion_lineal.pkl'")
