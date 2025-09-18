import os
from datetime import datetime

# Proje kök klasörünü bul
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_FILE = os.path.join(ROOT, "logs.txt")

def write_logs(message: str):
    """Log dosyasına mesaj ekle"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

def read_logs(limit: int = 50):
    """Log dosyasından son X satırı oku"""
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[-limit:]
