from sqlalchemy import or_
from database.connection import SessionLocal
from models.usuario import Usuario
from utils.security import verificar_password


def iniciar_sesion(usuario_o_email: str, password: str):
    db = SessionLocal()
    try:
        # Buscar usuario
        usuario = db.query(Usuario).filter(or_(Usuario.username == usuario_o_email, Usuario.email == usuario_o_email)).first()
        # Usuario inexistente
        if not usuario:
            return None
        # Usuario desactivado
        if not usuario.activo:
            return None
        # Comprobar contraseña
        if not verificar_password(password,usuario.password):
            return None
        return usuario
    finally:
        db.close()