from flask import Blueprint, request
from routes.auth import auth_controller

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    return auth_controller.register(request.get_json())

@auth_bp.route("/login", methods=["POST"])
def login():
    return auth_controller.login(request.get_json())