from flask import Flask, jsonify, request
from auth import auth_bp
from db import logs   # 👈 import logs collection

app = Flask(__name__)

# Register auth routes
app.register_blueprint(auth_bp, url_prefix="/auth")


@app.route("/")
def home():
    return jsonify({"message": "EDR Backend Running 🚀"})


# ✅ ADD THIS ROUTE
@app.route("/log", methods=["POST"])
def receive_log():
    data = request.json

    if not data:
        return jsonify({"error": "No data received"}), 400

    logs.insert_one(data)

    return jsonify({"message": "Log stored successfully"})


if __name__ == "__main__":
    app.run(debug=True)