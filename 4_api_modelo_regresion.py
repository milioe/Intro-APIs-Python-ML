import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Cargar el modelo entrenado de regresión lineal
with open("Misc/modelo_regresion_lineal.pkl", "rb") as f:
    model = pickle.load(f)

# Crear la API
app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener datos del cuerpo de la solicitud
    data = request.get_json()
    
    # Convertir los datos en un DataFrame
    try:
        X_pred = pd.DataFrame([data])
    except Exception as e:
        return jsonify({"error": f"Error al procesar los datos: {str(e)}"}), 400
    
    # Realizar predicción
    try:
        prediccion = model.predict(X_pred)
        return jsonify({"prediccion": prediccion[0]})
    except Exception as e:
        return jsonify({"error": f"Error al hacer la predicción: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
