from flask import Blueprint, request  # Blueprint organiza rutas, request obtiene datos del cliente
from routes.sensores import sensores_controller  # Importa el controlador de sensores
from flask_jwt_extended import jwt_required  # Decorador que protege rutas con autenticación JWT

sensores_bp = Blueprint("sensores", __name__)  
# Crea un Blueprint llamado "sensores" para agrupar estas rutas


@sensores_bp.route("/insert", methods=["POST"])  
# Endpoint: POST /sensores/insert → recibe datos de sensores para guardarlos
@jwt_required()  
#  SOLO usuarios autenticados (con token válido) pueden acceder
def insert():
    return sensores_controller.insert_data(request.get_json())  
    # Toma el JSON enviado por el frontend y lo manda al controller


@sensores_bp.route("/ultimo", methods=["GET"])  
# Endpoint: GET /sensores/ultimo → obtiene el último dato registrado
@jwt_required()  
#  SOLO usuarios autenticados (con token válido) pueden acceder
def ultimo():
    return sensores_controller.get_last()  
    # Llama al controller que trae el último registro


@sensores_bp.route("/historial", methods=["GET"])  
# Endpoint: GET /sensores/historial → obtiene todos los datos (histórico)
@jwt_required()  
#  SOLO usuarios autenticados (con token válido) pueden acceder
def historial():
    return sensores_controller.get_historial()  
    # Llama al controller que devuelve el historial


@sensores_bp.route("/stats", methods=["GET"])  
# Endpoint: GET /sensores/stats → obtiene estadísticas de los sensores
@jwt_required()  
#  SOLO usuarios autenticados (con token válido) pueden acceder
def stats():
    return sensores_controller.get_stats()  
    # Llama al controller que calcula y retorna estadísticas