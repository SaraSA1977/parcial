from typing import Tuple, Optional  # Permite tipar retornos (tupla: usuario o None + mensaje)
from contextlib import contextmanager  # Permite crear un manejador de contexto (como "with")
from db.db import SessionLocal  # Conexión a la base de datos
from db.models import User  # Modelo de la tabla usuarios


@contextmanager
def get_db():
    db = SessionLocal()  # Abre conexión a la base de datos
    try:
        yield db  # Entrega la conexión para usarla dentro de "with"
    finally:
        db.close()  # Cierra la conexión automáticamente (aunque haya error)


def get_all_users():
    with get_db() as db:  # Usa el manejador de contexto (abre y cierra solo)
        return db.query(User).all()  # Consulta todos los usuarios


# 🔐 LOGIN SIMPLE
def login_user(data) -> Tuple[Optional[User], dict]:
    # Retorna: (usuario o None, mensaje de error o None)

    email = (data.get("email") or "").strip()  # Obtiene email o string vacío y elimina espacios
    password = (data.get("password") or "").strip()  # Igual para contraseña

    if not email or not password:  # Validación básica
        return None, {"message": "Email y contraseña son requeridos"}  # Error si faltan datos

    with get_db() as db:  # Abre conexión segura a la BD
        user = db.query(User).filter(User.email == email).first()  
        # Busca usuario por email

        if not user:
            return None, {"message": "Usuario no encontrado"}  # Si no existe

        if user.password != password:
            return None, {"message": "Contraseña incorrecta"}  # Si contraseña no coincide

        return user, None  # Login correcto → retorna usuario sin error


# 🆕 CREAR USUARIO
def create_user(data):

    email = (data.get("email") or "").strip()  # Limpia email
    password = (data.get("password") or "").strip()  # Limpia contraseña

    if not email or not password:  # Validación
        return None, {"message": "Email y contraseña son requeridos"}  # Error si faltan

    with get_db() as db:  # Abre conexión segura

        exists = db.query(User).filter(User.email == email).first()  
        # Verifica si el usuario ya existe

        if exists:
            return None, {"message": "El usuario ya existe"}  # Evita duplicados

        user = User(
            email=email,  # Asigna email
            password=password  # Asigna contraseña (⚠️ texto plano)
        )

        db.add(user)  # Agrega usuario a la sesión
        db.commit()  # Guarda en la base de datos
        db.refresh(user)  # Refresca el objeto con datos actualizados (ej: id)

        return user, None  # Retorna usuario creado sin error