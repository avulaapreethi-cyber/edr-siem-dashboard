import random
from datetime import datetime

def generate_log():
    return {
        "timestamp": datetime.now().isoformat(),
        "src_ip": f"192.168.1.{random.randint(1,255)}",
        "protocol": random.choice(["TCP","UDP"]),
        "bytes": random.randint(100,10000)
    }

def detect_attack(log):
    alerts = []

    if log["bytes"] > 8000:
        alerts.append({"type":"DoS","msg":"High Traffic","time":log["timestamp"]})

    if log["protocol"] == "UDP" and log["bytes"] > 6000:
        alerts.append({"type":"UDP Flood","msg":"Flood detected","time":log["timestamp"]})

    return alerts