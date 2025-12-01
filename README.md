Aplicación de Validación de JSON con Gradio y Docker

Esta aplicación permite subir únicamente ficheros JSON, que serán validados e interpretados mediante un modelo simple en Python.
Incluye una interfaz web creada con Gradio y se ejecuta como un servicio Docker.

📁 Estructura del proyecto
📦 proyecto
 ├── app.py
 ├── Dockerfile
 ├── requirements.txt
 ├── samples/
 │     ├── grupo_musical.json
 │     ├── analitica_sangre.json
 │     └── receta.json

🧠 Descripción de la aplicación

La aplicación:

Acepta únicamente archivos JSON

Intenta cargarlos con json.load()

Muestra el contenido o los errores de validación

Funciona desde una interfaz web sencilla en Gradio

Está preparada para ejecutarse en contenedor Docker

El código usa módulos estándar de Python como uuid y os, que NO necesitan instalarse, ya que vienen incluidos en Python por defecto.

📦 Instalación sin Docker (opcional)
pip install -r requirements.txt
python app.py


La aplicación abrirá una interfaz Gradio en:

http://127.0.0.1:7860

🐳 Ejecución usando Docker
1️⃣ Construir la imagen

Desde la carpeta del proyecto:

docker build -t validador-json .

2️⃣ Ejecutar el contenedor
docker run -p 7860:7860 validador-json


La aplicación quedará disponible en:

http://localhost:7860

📂 Uso dentro de la aplicación

Abre la interfaz web generada por Gradio

Sube uno de los ficheros JSON situados en la carpeta samples

La aplicación mostrará:

El contenido cargado si es válido

Un mensaje de error si no es un JSON válido

📄 Dependencias

El archivo requirements.txt incluye:

gradio


Las librerías:

uuid

os

json

NO necesitan añadirse porque forman parte de la biblioteca estándar de Python.

🤖 Tecnologías utilizadas

Python

Gradio

Docker