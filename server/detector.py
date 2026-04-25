def detect_threat(data):
    suspicious = ["cmd.exe", "powershell.exe", "nmap.exe"]

    for p in data.get("processes", []):
        if p in suspicious:
            return "⚠️ Threat Detected"

    return "Normal"
