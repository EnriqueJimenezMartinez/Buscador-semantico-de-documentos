import json
import chromadb
import gradio as gr
import os
import uuid
cliente = chromadb.Client()
coleccion = cliente.create_collection(name="documents")

def cargar_jsons_iniciales():
    carpeta = "samples"
    archivos = ["grupo_musical.json", "analitica_sangre.json", "receta.json"]

    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)

        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)

            documento = json.dumps(datos)

            coleccion.add(
                documents=[documento],
                ids=[archivo],
                metadatas=[{"nombre_fichero": archivo}]
            )

            print(f"JSON cargado: {archivo}")

        except Exception as e:
            print(f"Error cargando {archivo}: {e}")

# Cargar los 3 JSON al iniciar
cargar_jsons_iniciales()

def subir_ficheros_json(lista_ficheros):
    if not lista_ficheros:
        return "No se ha subido ningún fichero."

    añadidos = 0
    errores = []

    for fichero in lista_ficheros:
        nombre = getattr(fichero, "name", "")
        # Comprobar extensión .json
        if not nombre.lower().endswith(".json"):
            errores.append(f"{nombre} -> formato no permitido (solo .json)")
            continue

        try:
            contenido_bytes = fichero.read()
            contenido_texto = contenido_bytes.decode("utf-8")
            datos = json.loads(contenido_texto)  # valida que sea JSON válido
            documento = json.dumps(datos) 

            id_unico = str(uuid.uuid4())

            coleccion.add(
                documents=[documento],
                ids=[id_unico],
                metadatas=[{"nombre_fichero": nombre}]
            )
            añadidos += 1

        except Exception as e:
            errores.append(f"{nombre} -> error: {e}")

    mensaje = f"Añadidos: {añadidos}."
    if errores:
        mensaje += " Errores: " + "; ".join(errores)
    return mensaje

def consultar_chromadb(pregunta):
    if not pregunta or pregunta.strip() == "":
        return "Debes escribir una pregunta."

    try:
        resultado = coleccion.query(
            query_texts=[pregunta],
            n_results=1
        )

        # resultado["documents"] = [[doc1, doc2, ...], ...]
        docs = resultado.get("documents", [[]])
        if docs and len(docs[0]) > 0 and docs[0][0] is not None:
            return docs[0][0]
        else:
            return "No se encontró información relacionada."

    except Exception as e:
        return f"Error en la consulta: {e}"

with gr.Blocks(title="Consulta de JSON con ChromaDB") as interfaz:

    gr.Markdown("# 🔎 Consulta semántica (solo JSON)")

    with gr.Tabs():

        with gr.Tab("Subir ficheros (.json únicamente)"):
            entrada_archivos = gr.Files(
                label="Sube uno o varios archivos JSON",
                file_types=[".json"]
            )
            boton_subir = gr.Button("Añadir a la colección")
            salida_subida = gr.Textbox(label="Estado de la operación")
            boton_subir.click(subir_ficheros_json, inputs=entrada_archivos, outputs=salida_subida)

        with gr.Tab("Consulta"):
            entrada_pregunta = gr.Textbox(label="Pregunta", placeholder="Escribe una pregunta aquí...")
            boton_buscar = gr.Button("Buscar documento más relevante")
            salida_respuesta = gr.Textbox(label="Documento más relevante")
            boton_buscar.click(consultar_chromadb, inputs=entrada_pregunta, outputs=salida_respuesta)

if __name__ == "__main__":
    interfaz.launch()
