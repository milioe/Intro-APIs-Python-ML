# 🚀👩‍💻 Intro a las APIs

### ¡Hola! 🌟

Bienvenid@ al repo de la clase de APIs de **Python: de cero a ML** por [Humberto Acevedo](https://github.com/BetoACE)

Aquí encontrarás todo lo que necesitas para convertirte en un máster de las APIs 💥

---

## ☎️ Contacto

¿Dudas, comentarios o solo quieres saludar? ¡Estoy aquí para ayudarte! 👇

✉️ **Email:** [emilio@milioe.com](mailto:emilio@milioe.com)  



## 🛠️ ¿Cómo correr los códigos?

1. Clona este repo, corre este comando en tu terminal o da click en `<> Code` (botón verde), descargar el ZIP y abrir la carpeta en VSC.
   ```bash
   git clone https://github.com/milioe/Intro-APIs-Python-ML.git
   ```
2. Abre VSC, lo puedes descagar desde [aca](https://code.visualstudio.com/download). Dejo el link a un [tutorial](https://youtu.be/-IyA_Yvs8IQ?si=DjgaJIntR7LMrh4J) para correr python  
3. Instala las dependencias que vienen en `requirements.txt` con el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```
4. ¡Corre los códigos!



## Recursos

* [Slides de la sesión]()
* [Documentación de API de Spotify](https://developer.spotify.com/documentation/web-api)
* [Documentación INEGI](https://www.inegi.org.mx/servicios/api_indicadores.html)
* [Documentación OpenAI](https://platform.openai.com/docs/overview)
* APIs para economistas
   - [Our World in Data](https://docs.owid.io/projects/etl/api/)
   - [World Bank](https://documents.worldbank.org/en/publication/documents-reports/api)
   - [Banxico](https://www.banxico.org.mx/SieAPIRest/service/v1/;jsessionid=0f6ca8d820f46bff5a9b9ee114a0)
   - [St. Louis](https://fred.stlouisfed.org/docs/api/fred/)



## 🧠 Explicación de los ejercicios:

<details>
<summary>API de saludo personalizada</summary>

En este ejercicio, construimos una API sencilla con Flask que saluda de forma personalizada a los usuarios. Vamos a desglosar las partes clave:

### 📌 Configuración inicial de Flask

Creamos nuestra aplicación con Flask.

```Python
from flask import Flask

app = Flask(__name__)
```


### 📌 Definición de la ruta `/saludo`

Creamos un endpoint que recibe solicitudes POST.

```Python
@app.route('/saludo', methods=['POST'])
def saludo():
    ...
```


### 📌 Obtención de datos desde la solicitud

Extraemos el nombre enviado por el cliente en formato JSON y asignamos un valor predeterminado si no se proporciona.

```Python
data = request.get_json()
nombre = data.get("nombre", "invitado")
```


### 📌 Respuesta personalizada

Devolvemos un saludo en formato JSON al cliente.

```Python
return jsonify({"mensaje": f"Hola, {nombre}!"})
```


### 🏃‍♂️ Ejecución del servidor

Iniciamos la aplicación para probar la API localmente.

```Python
if __name__ == '__main__':
    app.run(debug=True)
```

### 🚀 **Prueba la API:**

Puedes probar el endpoint enviando una solicitud POST con un JSON al endpoint `http://127.0.0.1:5000/saludo`.

Ejemplo:
```Python
{
    "nombre": "Carlos"
}
```

Esto devolverá algo como:

```Python
{
    "mensaje": "Hola, Carlos!"
}
```

</details>


<details>
<summary>API de suma de números</summary>

En este ejercicio, construimos una API con Flask que realiza la suma de dos números proporcionados por el usuario. Desglosamos las partes clave a continuación:

### 📌 Configuración inicial de Flask

Creamos nuestra aplicación con Flask.

```Python
from flask import Flask

app = Flask(__name__)
```


### 📌 Definición de la ruta `/suma`

Creamos un endpoint que recibe solicitudes POST para realizar la suma.

```Python
@app.route('/suma', methods=['POST'])
def suma():
    ...
```


### 📌 Obtención de datos desde la solicitud

Extraemos los números enviados por el cliente en formato JSON.

```Python
data = request.get_json()
num1 = data.get("num1")
num2 = data.get("num2")
```


### 📌 Realizar la suma

Convertimos los valores a flotantes (para permitir decimales) y realizamos la operación de suma.

```Python
resultado = float(num1) + float(num2)
```


### 📌 Respuesta al cliente

Devolvemos el resultado de la suma en formato JSON.

```Python
return jsonify({"resultado": resultado})
```


### 🏃‍♂️ Ejecución del servidor

Iniciamos la aplicación para probar la API localmente.

```Python
if __name__ == '__main__':
    app.run(debug=True)
```


### 🚀 **Prueba la API:**

Puedes probar el endpoint enviando una solicitud POST con un JSON al endpoint `http://127.0.0.1:5000/suma`.

Ejemplo:
```Python
{
    "num1": 5,
    "num2": 3.2
}
```

Esto devolverá algo como:

```Python
{
    "resultado": 8.2
}
```

</details>


<details>
<summary>API de operaciones matemáticas (diferentes endpoints)</summary>

Esta API, construida con Flask, realiza operaciones básicas como suma, resta, multiplicación y división. Cada operación tiene su propio endpoint y maneja casos de errores como datos inválidos o división entre cero.

### 📌 ¿Cómo funciona?

1. Se define un endpoint para cada operación: `/suma`, `/resta`, `/multiplicacion` y `/division`.
2. La API recibe dos números en formato JSON como entrada.
3. Realiza la operación solicitada y devuelve el resultado en formato JSON.
4. Si hay un error (como datos no válidos o división entre cero), devuelve un mensaje de error con el código HTTP correspondiente.


### 📌 Ejemplo de solicitud:

**Entrada (JSON):**
```Python
{
    "num1": 10,
    "num2": 5
}
```

**Salida esperada para `/suma`:**
```Python
{
    "resultado": 15
}
```

</details>


<details>
<summary>API de predicción con modelo de Machine Learning</summary>

Esta API utiliza Flask para exponer un modelo de regresión lineal previamente entrenado y guardado en un archivo `.pkl`. Permite realizar predicciones basadas en los datos enviados por el usuario.


### 📌 ¿Cómo funciona?

1. **Carga del modelo:**  
   El modelo de regresión lineal se carga desde un archivo serializado (`modelo_regresion_lineal.pkl`) usando la librería `pickle`.

```Python
with open("Misc/modelo_regresion_lineal.pkl", "rb") as f:
    model = pickle.load(f)
```

2. **Definición del endpoint `/predecir`:**  
   Este endpoint acepta solicitudes POST, recibe datos en formato JSON y los convierte a un DataFrame para realizar predicciones.

```Python
@app.route('/predecir', methods=['POST'])
def predecir():
    ...
```

3. **Flujo de predicción:**
   - Los datos enviados se convierten en un DataFrame.
   - El modelo hace la predicción usando los datos procesados.
   - El resultado de la predicción se devuelve como respuesta JSON.


### 📌 Manejo de errores

- Si los datos enviados no pueden procesarse correctamente, la API devuelve un error 400 con un mensaje descriptivo.
- Si ocurre un error al realizar la predicción, la API devuelve un error 500 con detalles del problema.


### 📌 Ejemplo de solicitud:

**Entrada (JSON):**
```Python
{
    "feature1": 1.2,
    "feature2": 3.4,
    "feature3": 5.6
}
```

**Salida esperada:**
```Python
{
    "prediccion": 42.7
}
```

**Si hay un error en los datos:**  
```Python
{
    "error": "Error al procesar los datos: ..."
}
```

Esta API es una base poderosa para integrar modelos de Machine Learning en aplicaciones reales. 🚀

</details>








## 🎧 Chill & Code
Mientras creaba los contenidos de esta sesión escuchaba [este EP](https://open.spotify.com/intl-es/album/353uBBfNLMFgXDJkTWSpWe?si=w0o0_HOOTF-MIjuiRbPMJA)
