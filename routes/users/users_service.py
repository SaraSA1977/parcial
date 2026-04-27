from typing import Tuple, Optional
from contextlib import contextmanager
from db.db import SessionLocal
from db.models import User


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_all_users():
    with get_db() as db:
        return db.query(User).all()


# 🔐 LOGIN SIMPLE
def login_user(data) -> Tuple[Optional[User], dict]:

    email = (data.get("email") or "").strip()
    password = (data.get("password") or "").strip()

    if not email or not password:
        return None, {"message": "Email y contraseña son requeridos"}

    with get_db() as db:
        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None, {"message": "Usuario no encontrado"}

        if user.password != password:
            return None, {"message": "Contraseña incorrecta"}

        return user, None


# 🆕 CREAR USUARIO
def create_user(data):

    email = (data.get("email") or "").strip()
    password = (data.get("password") or "").strip()

    if not email or not password:
        return None, {"message": "Email y contraseña son requeridos"}

    with get_db() as db:

        exists = db.query(User).filter(User.email == email).first()
        if exists:
            return None, {"message": "El usuario ya existe"}

        user = User(
            email=email,
            password=password
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user, None