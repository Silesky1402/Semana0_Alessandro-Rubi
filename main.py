from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import chat
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI()

# Definir clase para entrada de datos


class Consulta(BaseModel):
    pregunta: str

# Endpoint raíz para verificar que la API está activa


@app.get("/")
def inicio():
    return {"texto": "API de consultas activa"}

# Endpoint para resolver consultas utilizando el modelo Ollama


@app.post("/resolver")
def preguntar(input: Consulta):
    try:
        consulta = [{"role": "user", "content": input.pregunta}]
        # Recuperar configuración desde variables de entorno
        # Modelo por defecto si no se encuentra la variable
        modelo = os.getenv("OLLAMA_MODEL")
        respuesta = chat(modelo, consulta)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error : {str(e)}"
        )

# Endpoint para mostrar información de usuarios (ejemplo básico)


@app.get("/usuarios/{id}")
def mostrar_usuario(id: int):
    return {"data": id}
