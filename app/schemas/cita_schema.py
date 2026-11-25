from pydantic import BaseModel, ConfigDict, Field


class CrearCita(BaseModel):
    nombre: str = Field(min_length=3, max_length=25)
    descripcion: str = Field(max_length=150)
    fecha: str = Field(max_length=50)
    hora: str = Field(max_length=10)
    lugar: str = Field(max_length=150)


class RespuestaCita(BaseModel):
    id: int
    nombre: str
    descripcion: str
    fecha: str
    hora: str
    lugar: str

    model_config = ConfigDict(from_attributes=True)
