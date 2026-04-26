from routes.auth import auth_service
from flask_jwt_extended import create_access_token

def register(data):
    user = auth_service.create_user(data)
    return {"msg": "Usuario creado"}


def login(data):
    user = auth_service.login_user(data)

    if not user:
        return {"error": "Credenciales incorrectas"}, 401

    token = create_access_token(identity=user.id)

    return {
        "token": token
    }