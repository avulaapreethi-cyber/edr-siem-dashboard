from flask import Blueprint, request, jsonify
from db import logs
from datetime import datetime

routes_bp = Blueprint("routes", __name__)

# ADD LOG
@routes_bp.route("/log", methods=["POST"])
def add_log():
    data = request.get_json()

    log = {
        "timestamp": datetime.now().isoformat(),
        "source_ip": data.get("source_ip"),
        "event": data.get("event"),
        "status": data.get("status")
    }

    logs.insert_one(log)

    return jsonify({"message": "Log stored successfully"})


# GET LOGS
@routes_bp.route("/logs", methods=["GET"])
def get_logs():
    all_logs = list(logs.find({}, {"_id": 0}))
    return jsonify(all_logs)


# ALERTS (basic detection)
@routes_bp.route("/alerts", methods=["GET"])
def get_alerts():
    suspicious = list(logs.find({
        "event": {"$in": ["DoS", "Brute Force"]}
    }, {"_id": 0}))

    return jsonify(suspicious)