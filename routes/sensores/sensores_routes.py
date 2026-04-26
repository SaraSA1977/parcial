from flask import Blueprint, request
from routes.sensores import sensores_controller

sensores_bp = Blueprint("sensores", __name__)

@sensores_bp.route("/insert", methods=["POST"])
def insert():
    return sensores_controller.insert_data(request.get_json())

@sensores_bp.route("/ultimo", methods=["GET"])
def ultimo():
    return sensores_controller.get_last()

@sensores_bp.route("/historial", methods=["GET"])
def historial():
    return sensores_controller.get_historial()

@sensores_bp.route("/stats", methods=["GET"])
def stats():
    return sensores_controller.get_stats()