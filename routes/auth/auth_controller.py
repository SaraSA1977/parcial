from routes.auth import auth_service  # Importa el servicio de autenticación donde está la lógica de negocio (crear usuario, validar login)
from flask_jwt_extended import create_access_token  # Función que permite generar el token JWT cuando el usuario inicia sesión correctamente


def register(data):  # Función que maneja el registro de usuario (recibe datos desde el controller/ruta)

    user = auth_service.create_user(data)  # Llama al service para crear el usuario en la base de datos

    return {"msg": "Usuario creado"}  # Devuelve un mensaje de confirmación al frontend


def login(data):   # Función que maneja el inicio de sesión

    user = auth_service.login_user(data)   # Llama al service para validar las credenciales (usuario y contraseña)

    if not user:   # Si el usuario no existe o la contraseña es incorrecta

        return {"error": "Credenciales incorrectas"}, 401   # Devuelve error con código HTTP 401 (no autorizado)

    token = create_access_token(identity=str(user.id))   # Si el login es correcto, genera un token JWT
    # "identity" guarda el identificador del usuario (en este caso el id)

    return {
        "token": token
    }  
    # Devuelve el token al frontend para futuras peticiones autenticadas