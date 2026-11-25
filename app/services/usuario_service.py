from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from app.models.usuario import Usuario
from app.schemas.usuario_schema import CrearUsuario

password_hash = PasswordHash.recommended()


def consultar_usuarios(db: Session):
    return db.query(Usuario).all()


def consultar_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def consultar_correo(db: Session, correo: str, usuario_id: int = None):
    consulta = db.query(Usuario).filter(Usuario.correo == correo)

    if usuario_id is not None:
        consulta = consulta.filter(Usuario.id != usuario_id)

    return consulta.first()


def registrar_usuario(db: Session, data: CrearUsuario):
    correo_normalizado = data.correo.lower().strip()

    usuario = Usuario(
        nombre=data.nombre.strip(),
        correo=correo_normalizado,
        contrasena_hash=password_hash.hash(data.contrasena)
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


def actualizar_usuario(db: Session, usuario: Usuario, data: CrearUsuario):
    usuario.nombre = data.nombre.strip()
    usuario.correo = data.correo.lower().strip()
    usuario.contrasena_hash = password_hash.hash(data.contrasena)

    db.commit()
    db.refresh(usuario)

    return usuario


def eliminar_usuario(db: Session, usuario: Usuario):
    db.delete(usuario)
    db.commit()

    return {"message": "El usuario fue eliminado"}
