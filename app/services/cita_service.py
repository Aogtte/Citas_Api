from sqlalchemy.orm import Session
from app.models.cita import Cita
from app.schemas.cita_schema import CrearCita


def consultar_citas(db: Session):
    return db.query(Cita).all()


def consultar_citas_fecha(db: Session, fecha: str):
    return db.query(Cita).filter(Cita.fecha == fecha).all()


def consultar_cita(db: Session, cita_id: int):
    return db.query(Cita).filter(Cita.id == cita_id).first()


def crear_cita(db: Session, data: CrearCita):
    cita = Cita(
        nombre=data.nombre,
        descripcion=data.descripcion,
        fecha=data.fecha,
        hora=data.hora,
        lugar=data.lugar
    )

    db.add(cita)
    db.commit()
    db.refresh(cita)

    return cita


def actualizar_cita(db: Session, cita: Cita, data: CrearCita):
    cita.nombre = data.nombre
    cita.descripcion = data.descripcion
    cita.fecha = data.fecha
    cita.hora = data.hora
    cita.lugar = data.lugar

    db.commit()
    db.refresh(cita)

    return cita


def eliminar_cita(db: Session, cita: Cita):
    db.delete(cita)
    db.commit()

    return {"message": "La cita fue eliminada"}
