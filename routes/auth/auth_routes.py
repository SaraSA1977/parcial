from flask import Blueprint, request  # Blueprint permite modularizar rutas, request obtiene datos de la petición

from routes.auth import auth_controller  # Importa el controlador que maneja la lógica de auth

auth_bp = Blueprint("auth", __name__)  
# Crea un Blueprint llamado "auth" para agrupar todas las rutas de autenticación

@auth_bp.route("/register", methods=["POST"])  
# Define el endpoint /register que acepta peticiones POST (crear usuario)
def register():
    return auth_controller.register(request.get_json())  
    # Obtiene el JSON enviado desde el frontend y lo envía al controller
    # El controller se encarga de procesar y devolver la respuesta

@auth_bp.route("/login", methods=["POST"])  
# Define el endpoint /login que acepta peticiones POST (iniciar sesión)
def login():
    return auth_controller.login(request.get_json())  
    # Obtiene los datos del login (usuario, contraseña)
    # Llama al controller que valida y genera el token JWT