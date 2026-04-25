import requests
import time
import random

while True:
    log = {
        "timestamp": time.ctime(),
        "ip": "192.168.1." + str(random.randint(1,255)),
        "attack": random.choice(["Normal","DoS","Probe"])
    }

    try:
        requests.post("http://127.0.0.1:5000/log", json=log)
    except:
        print("Server not running")

    time.sleep(2)