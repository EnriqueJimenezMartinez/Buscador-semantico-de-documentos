# 📄 Validador de JSON con Gradio y Docker

Esta aplicación permite subir archivos **JSON**, que serán validados e interpretados mediante un modelo simple en Python.  
Incluye una interfaz web creada con **Gradio** y puede ejecutarse dentro de un contenedor **Docker**.

---

## ⚙️ Requisitos

Para ejecutar el proyecto necesitas tener instalado:

- Python 3.8 o superior
- Librerías principales:
  - `gradio`
- Librerías estándar de Python (no requieren instalación):
  - `os`
  - `uuid`
  - `json`

---

## 🚀 Uso

### Sin Docker

1. Clona el repositorio:

```bash
git clone 
Accede a la carpeta del proyecto: 
https://github.com/EnriqueJimenezMartinez/Buscador-semantico-de-documentos.git
cd Buscador-semantico-de-documentos
Instala las dependencias:

pip install -r requirements.txt
Ejecuta la aplicación:

python app.py
La interfaz web de Gradio se abrirá en:

http://127.0.0.1:7860
````
---

### Con Docker
```bash
Construir la imagen:

docker build -t validador-json .
Ejecutar el contenedor:

docker run -p 7860:7860 validador-json
La aplicación quedará disponible en:

http://localhost:7860
📂 Uso dentro de la aplicación
Abre la interfaz web generada por Gradio.

Sube uno de los archivos JSON situados en la carpeta samples.
```
La aplicación mostrará:

El contenido cargado si es válido.

Un mensaje de error si no es un JSON válido.

🗂️ Estructura del proyecto
```bash
proyecto/
├── app.py
├── Dockerfile
├── requirements.txt
├── samples/
│   ├── grupo_musical.json
│   ├── analitica_sangre.json
│   └── receta.json

```
## 📌 Objetivos del proyecto
Validar archivos JSON de manera sencilla y rápida.

Mostrar errores claros en caso de JSON inválido.

Proporcionar una interfaz web fácil de usar con Gradio.

Facilitar la ejecución en cualquier sistema usando Docker.

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, siempre citando la fuente.

## 👨‍💻 Autor
Enrique Jiménez Martínez
