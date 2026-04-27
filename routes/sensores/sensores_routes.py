from flask import Blueprint, request
from routes.sensores import sensores_controller
from flask_jwt_extended import jwt_required

sensores_bp = Blueprint("sensores", __name__)

@sensores_bp.route("/insert", methods=["POST"])
@jwt_required()
def insert():
    return sensores_controller.insert_data(request.get_json())


@sensores_bp.route("/ultimo", methods=["GET"])
@jwt_required()
def ultimo():
    return sensores_controller.get_last()


@sensores_bp.route("/historial", methods=["GET"])
@jwt_required()
def historial():
    return sensores_controller.get_historial()


@sensores_bp.route("/stats", methods=["GET"])
@jwt_required()
def stats():
    return sensores_controller.get_stats()