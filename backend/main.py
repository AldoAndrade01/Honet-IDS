# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scanner import escanear_red  # Importamos tu módulo

app = FastAPI()

# Configurar CORS para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Bienvenido a Honet-IDS API"}

@app.get("/dispositivos")
def get_dispositivos():
    try:
        dispositivos = escanear_red()
        return dispositivos
    except Exception as e:
        return {"error": str(e)}
