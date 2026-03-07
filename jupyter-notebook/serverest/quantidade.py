import time
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os

URL = "https://serverest.dev/usuarios"
INTERVALO = 60
CSV_FILE = "usuarios_monitoramento.csv"

valores = []
tempos = []

plt.ion()
fig, ax = plt.subplots()

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "hora", "total"])

try:
    while True:
        response = requests.get(URL, timeout=10)
        data = response.json()

        total = data["quantidade"]
        agora = datetime.now()

        hora_str = agora.strftime("%H:%M:%S")
        timestamp = int(agora.timestamp())

        valores.append(total)
        tempos.append(hora_str)

        print(f"{hora_str} | Total usuários: {total}")

        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, hora_str, total])

        ax.clear()
        ax.plot(tempos, valores, marker="o")
        ax.set_title("Monitoramento de Usuários")
        ax.set_xlabel("Tempo")
        ax.set_ylabel("Quantidade")
        ax.grid(True)

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(0.1)

        time.sleep(INTERVALO)

except KeyboardInterrupt:
    print("\nEncerrando monitoramento...")

finally:
    plt.ioff()
    plt.close("all")