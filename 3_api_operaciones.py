from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    try:
        resultado = float(num1) + float(num2)
        return jsonify({"resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Proporciona números válidos"}), 400


@app.route('/resta', methods=['POST'])
def resta():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    try:
        resultado = float(num1) - float(num2)
        return jsonify({"resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Proporciona números válidos"}), 400


@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    try:
        resultado = float(num1) * float(num2)
        return jsonify({"resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Proporciona números válidos"}), 400


@app.route('/division', methods=['POST'])
def division():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    try:
        if float(num2) == 0:
            return jsonify({"error": "No se puede dividir entre cero"}), 400
        resultado = float(num1) / float(num2)
        return jsonify({"resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Proporciona números válidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)
