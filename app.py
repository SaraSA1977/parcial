import os  # Permite acceder a variables del sistema (como las del .env)

from flask import Flask  # Importa la clase principal para crear la app Flask
from flask_cors import CORS  # Permite la comunicación entre frontend y backend (CORS)
from dotenv import load_dotenv  # Carga las variables del archivo .env
from flask_jwt_extended import JWTManager  # Maneja autenticación con tokens JWT

# NUESTRAS RUTAS CRUD
from routes.auth.auth_routes import auth_bp  # Importa rutas de autenticación
from routes.sensores.sensores_routes import sensores_bp  # Importa rutas de sensores
from routes.users.users_routes import users_bp  # Importa rutas de usuarios

from datetime import timedelta  # Permite manejar tiempos (para expiración de tokens)

def run_app():  # Función que configura y crea la aplicación
    load_dotenv()  # Carga las variables del archivo .env

    app = Flask(__name__)  # Crea la instancia de la aplicación Flask

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")  
    # Define la clave secreta para firmar los tokens JWT (se toma del .env)

    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
        minutes=int(os.getenv("JWT_EXPIRES_MIN", 1))
    )
    # Define cuánto tiempo dura el token (en minutos)
    # Si no hay variable en .env, usa 1 minuto por defecto

    jwt = JWTManager(app)  
    # Inicializa el sistema JWT en la aplicación

    # Configuración CORS
    CORS(
        app,
        resources={r"/*": {"origins": "*"}},  # Permite acceso desde cualquier origen (frontend)
        supports_credentials=False,  # No permite envío de cookies o credenciales
        expose_headers=["Authorization"],  # Permite que el frontend lea el header Authorization
        allow_headers=["Content-Type", "Authorization"],  # Headers permitidos en requests
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]  # Métodos HTTP permitidos
    )

    ## registrar rutas CRUD de tus tablas
    app.register_blueprint(auth_bp, url_prefix="/auth")  
    # Registra rutas de autenticación con prefijo /auth

    app.register_blueprint(sensores_bp, url_prefix="/sensores")  
    # Registra rutas de sensores con prefijo /sensores

    app.register_blueprint(users_bp, url_prefix="/users")  
    # Registra rutas de usuarios con prefijo /users

    return app  # Retorna la aplicación ya configurada

app = run_app()  # Ejecuta la función y crea la app

if __name__ == "__main__":  # Se ejecuta solo si corres este archivo directamente
    app.run(
        host=os.getenv("HOST", "127.0.0.1"),  # Dirección del servidor (por defecto localhost)
        port=int(os.getenv("PORT", 5000)),  # Puerto (por defecto 5000)
        debug=True  # Activa modo desarrollo (muestra errores y recarga automática)
    )