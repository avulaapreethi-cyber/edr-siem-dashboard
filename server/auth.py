from flask import Blueprint, request, jsonify
from db import users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    user = {
        "username": data.get("username"),
        "password": data.get("password")
    }

    users.insert_one(user)

    return jsonify({"message": "User registered successfully"})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    user = users.find_one({
        "username": data.get("username"),
        "password": data.get("password")
    })

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"}), 401