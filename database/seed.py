from database.connection import SessionLocal
from models.rol import Rol
from models.usuario import Usuario
from utils.security import hashear_password


def seed_database():

    db = SessionLocal()

    try:
        # Hashear contraseña del usuario existente
        usuario = db.query(Usuario).filter_by(id=1).first()
        if usuario:
            if not usuario.password.startswith("$2b$"):
                usuario.password = hashear_password(usuario.password)
                db.commit()
        # Roles
        roles = [
            "Administrador",
            "Cajero"
        ]

        for nombre in roles:
            existe = db.query(Rol).filter_by(
                nombre=nombre
            ).first()
            if not existe:
                db.add(
                    Rol(nombre=nombre)
                )
        db.commit()
        # Usuario administrador
        rol_admin = db.query(Rol).filter_by(
            nombre="Administrador"
        ).first()
        usuario_admin = db.query(Usuario).filter_by(
            username="fcabrera8839"
        ).first()
        if not usuario_admin:
            usuario_admin = Usuario(
                username="fcabrera8839",
                password=hashear_password("admin123"),
                nombre="Fernando",
                apellido="Cabrera",
                email="cabrerafernando743@gmail.com",
                rol_id=rol_admin.id,
                activo=True
            )
            db.add(usuario_admin)
            db.commit()
    except Exception as error:
        db.rollback()
        print(f"Error al cargar datos: {error}")
        raise
    finally:
        db.close()