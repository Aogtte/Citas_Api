from sqlalchemy import Column, Integer, String
from app.database.conexion import Base


class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(25), nullable=False)
    descripcion = Column(String(150), nullable=False)
    fecha = Column(String(50), nullable=False)
    hora = Column(String(10), nullable=False)
    lugar = Column(String(150), nullable=False)
