from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import chat
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir clase para entrada de datos


class Consulta(BaseModel):
    pregunta: str

# Este endpoint devuelve un mensaje indicando que la API está funcionando correctamente.


@app.get("/", response_class=JSONResponse)
def inicio():

    return JSONResponse(content={"texto": "API de consultas activa"}, status_code=200)


# Este endpoint recibe una consulta, la envía al modelo Ollama, y devuelve la respuesta.

@app.post("/resolver", response_class=JSONResponse)
def preguntar(input: Consulta):
    try:
        # Imprimir la solicitud recibida.
        print("Solicitud recibida:", input.pregunta)

        # Construir la consulta para enviarla al modelo Ollama.
        consulta = [{"role": "user", "content": input.pregunta}]

        # Recuperar el nombre del modelo desde las variables de entorno.
        # Si la variable no está configurada, se utiliza un valor por defecto ("default_model").
        modelo = os.getenv("OLLAMA_MODEL", "default_model")
        if modelo is None or modelo == "default_model":
            # Lanzar un error si el modelo no está configurado correctamente.
            raise ValueError("El modelo no está configurado correctamente.")
        # Imprimir el modelo utilizado.
        print("Modelo usado:", modelo)

        # Llamar al modelo Ollama para obtener la respuesta.
        respuesta_completa = chat(modelo, consulta)

        # Extraer únicamente el contenido serializable de la respuesta.
        respuesta = respuesta_completa.message.content

        # Imprimir la respuesta del modelo.
        print("Respuesta del modelo:", respuesta)

        # Devolver la respuesta en formato JSON al cliente.
        return JSONResponse(content={"respuesta": respuesta}, status_code=200)

    except ValueError as ve:
        # Manejar errores específicos relacionados con configuraciones incorrectas.
        # Imprimir el error para depuración.
        print("Error de configuración:", str(ve))
        return JSONResponse(
            content={"error": f"Error de configuración: {str(ve)}"},
            status_code=500
        )
    except Exception as e:
        # Capturar otros errores y devolverlos al cliente.
        print("Error ocurrido:", str(e))  # Log general del error en consola.
        return JSONResponse(
            content={"error": f"Error interno: {str(e)}"},
            status_code=500
        )

# Endpoint para mostrar información de usuarios
# Este endpoint devuelve información básica basada en un ID proporcionado en la URL.


@app.get("/usuarios/{id}", response_class=JSONResponse)
def mostrar_usuario(id: int):
    try:

        return JSONResponse(content={"data": {"id_usuario": id}}, status_code=200)
    except Exception as e:
        # Maneja errores generales y lanza una excepción HTTP con un código de estado 500.
        raise HTTPException(
            status_code=500,
            detail={"error": f"Error interno: {str(e)}"}
        )
