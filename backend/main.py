from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir conexión desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy endpoint
@app.get("/alertas")
def get_alertas():
    return [{"ip": "192.168.0.23", "riesgo": 0.91}]