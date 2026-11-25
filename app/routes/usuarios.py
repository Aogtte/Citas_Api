from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.schemas.usuario_schema import CrearUsuario, RespuestaUsuario
from app.services import usuario_service

router = APIRouter()


# POST: Registrar un usuario
@router.post("/", response_model=RespuestaUsuario, status_code=201)
def registrar_usuario(
    data: CrearUsuario,
    db: Session = Depends(get_db)
):
    correo_normalizado = data.correo.lower().strip()
    existente = usuario_service.consultar_correo(db, correo_normalizado)

    if existente is not None:
        raise HTTPException(
            status_code=400,
            detail="El correo electrónico ya está registrado"
        )

    return usuario_service.registrar_usuario(db, data)


# GET: Consultar todos los usuarios
@router.get("/", response_model=list[RespuestaUsuario])
def consultar_usuarios(db: Session = Depends(get_db)):
    return usuario_service.consultar_usuarios(db)


# GET: Consultar un usuario por ID
@router.get("/{usuario_id}", response_model=RespuestaUsuario)
def consultar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = usuario_service.consultar_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ningún usuario"
        )

    return usuario


# PUT: Actualizar un usuario
@router.put("/{usuario_id}", response_model=RespuestaUsuario)
def actualizar_usuario(
    usuario_id: int,
    data: CrearUsuario,
    db: Session = Depends(get_db)
):
    usuario = usuario_service.consultar_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ningún usuario"
        )

    correo_normalizado = data.correo.lower().strip()
    duplicado = usuario_service.consultar_correo(
        db,
        correo_normalizado,
        usuario_id
    )

    if duplicado is not None:
        raise HTTPException(
            status_code=400,
            detail="El correo electrónico ya está registrado por otro usuario"
        )

    return usuario_service.actualizar_usuario(db, usuario, data)


# DELETE: Eliminar un usuario
@router.delete("/{usuario_id}")
def eliminar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = usuario_service.consultar_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ningún usuario"
        )

    return usuario_service.eliminar_usuario(db, usuario)
