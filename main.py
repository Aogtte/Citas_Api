from fastapi import FastAPI

from app.database.conexion import Base, engine
from app.models.cita import Cita
from app.models.usuario import Usuario
from app.routes import citas, usuarios


# Crear las tablas en Neon si todavía no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Citas API")

# Registrar las rutas de cada módulo
app.include_router(citas.router, prefix="/citas", tags=["Citas"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
