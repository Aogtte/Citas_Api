from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.schemas.cita_schema import CrearCita, RespuestaCita
from app.services import cita_service

router = APIRouter()


# GET: Consultar todas las citas
@router.get("/", response_model=list[RespuestaCita])
def consultar_citas(db: Session = Depends(get_db)):
    return cita_service.consultar_citas(db)


# GET: Consultar citas por fecha
@router.get("/fecha", response_model=list[RespuestaCita])
def consultar_cita_fecha(
    cita_fecha: str,
    db: Session = Depends(get_db)
):
    citas = cita_service.consultar_citas_fecha(db, cita_fecha)

    if not citas:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ninguna cita con esa fecha"
        )

    return citas


# GET: Consultar una cita por ID
@router.get("/{cita_id}", response_model=RespuestaCita)
def consultar_cita(
    cita_id: int,
    db: Session = Depends(get_db)
):
    cita = cita_service.consultar_cita(db, cita_id)

    if cita is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ninguna cita"
        )

    return cita


# POST: Registrar una cita
@router.post("/", response_model=RespuestaCita, status_code=201)
def crear_cita(
    data: CrearCita,
    db: Session = Depends(get_db)
):
    return cita_service.crear_cita(db, data)


# PUT: Actualizar una cita
@router.put("/{cita_id}", response_model=RespuestaCita)
def actualizar_cita(
    cita_id: int,
    data: CrearCita,
    db: Session = Depends(get_db)
):
    cita = cita_service.consultar_cita(db, cita_id)

    if cita is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ninguna cita"
        )

    return cita_service.actualizar_cita(db, cita, data)


# DELETE: Eliminar una cita
@router.delete("/{cita_id}")
def eliminar_cita(
    cita_id: int,
    db: Session = Depends(get_db)
):
    cita = cita_service.consultar_cita(db, cita_id)

    if cita is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ninguna cita"
        )

    return cita_service.eliminar_cita(db, cita)
