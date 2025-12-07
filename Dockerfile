FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
# Directorio de trabajo dentro del contenedor
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 7860
# Permitimos que Gradio sea accesible desde fuera del contenedor
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Ejecutar la app
CMD ["python", "app.py"]
