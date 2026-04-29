from db.db import SessionLocal  
# Importa la fábrica de sesiones para conectarse a la base de datos

from db.models import User  
# Importa el modelo User (representa la tabla de usuarios en la BD)


def create_user(data):  
    # Función para crear un nuevo usuario en la base de datos

    db = SessionLocal()  
    # Abre una sesión/conexión con la base de datos

    user = User(
        email=data["email"],  # Asigna el email recibido desde el frontend
        password=data["password"]  # Asigna la contraseña (⚠️ ahora mismo está en texto plano)
    )

    db.add(user)  
    # Agrega el nuevo usuario a la sesión (aún no se guarda en la BD)

    db.commit()  
    # Confirma la transacción y guarda el usuario en la base de datos

    db.close()  
    # Cierra la conexión con la base de datos

    return user  
    # Retorna el usuario creado


def login_user(data):  
    # Función para validar las credenciales del usuario

    db = SessionLocal()  
    # Abre una sesión con la base de datos

    user = db.query(User).filter(User.email == data["email"]).first()  
    # Busca un usuario en la BD cuyo email coincida con el enviado

    if user and user.password == data["password"]:  
        # Verifica:
        # 1. Que el usuario exista
        # 2. Que la contraseña coincida

        return user  
        # Si todo es correcto, retorna el usuario

    return None  
    # Si falla, retorna None (login inválido)