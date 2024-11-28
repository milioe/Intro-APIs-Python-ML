from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saludo', methods=['POST'])
def saludo():
    
    # Obtener datos JSON del cuerpo de la solicitud
    data = request.get_json()
    
    # Extraer el nombre del JSON (con valor predeterminado si no está)
    nombre = data.get("nombre")
    return jsonify({"mensaje": f"Hola, {nombre}!"})

if __name__ == '__main__':
    app.run(debug=True)
