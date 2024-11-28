from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma():
    # Obtener datos JSON del cuerpo de la solicitud
    data = request.get_json()
    
    # Extraer los números (con validación básica)
    num1 = data.get("num1")
    num2 = data.get("num2")
    
    # Convertir a flotante para permitir decimales
    resultado = float(num1) + float(num2)
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)