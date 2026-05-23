"""API Flask sencilla: recibe datos del cliente y devuelve la predicción."""

import pickle
import warnings
from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, request

warnings.filterwarnings("ignore", category=UserWarning)

MODELS_PATH = Path(__file__).parent / "models"


def load_models():
    """Carga modelo, scaler, encoders y features de clasificación."""
    def _load(name):
        with open(MODELS_PATH / name, "rb") as f:
            return pickle.load(f)

    return {
        "modelo": _load("clasificacion_modelo_banco.pkl"),
        "scaler": _load("clasificacion_scaler_banco.pkl"),
        "encoders": _load("clasificacion_encoders_banco.pkl"),
        "features": _load("clasificacion_features_banco.pkl"),
    }


def predecir(data: dict, models: dict) -> int:
    """Recibe los datos del cliente y devuelve 0 o 1."""
    df = pd.DataFrame([data])

    for col, encoder in models["encoders"].items():
        if col in df.columns:
            if df[col].iloc[0] in encoder.classes_:
                df[col] = encoder.transform(df[col])
            else:
                df[col] = 0

    X = models["scaler"].transform(df[models["features"]])
    return int(models["modelo"].predict(X)[0])


app = Flask(__name__)
models = load_models()


@app.route("/predict", methods=["POST"])
def predict():
    """
    Predice si un cliente contratará un depósito a plazo.

    Envía un JSON con los parámetros del cliente y recibe:
    {"prediccion": 0}  → no contratará
    {"prediccion": 1}  → sí contratará
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Envía los datos en JSON"}), 400

    try:
        prediccion = predecir(data, models)
        return jsonify({"prediccion": prediccion})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
