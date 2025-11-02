import random
import time
import requests

CLIENTS = ["Sao Paulo", "Salvador", "Rio de Janeiro", "Santa Catarina", "Belo Horizonte"]
BASE_URL = "http://localhost:8080/flow"
RUN_DURATION = 60 * 10  # 2 minutos, ajuste como quiser
END_PROBABILITY = 0.7


def simulate():
    end_time = time.time() + RUN_DURATION
    print(f"🚀 Iniciando simulação de fluxos por {RUN_DURATION} segundos...\n")

    while time.time() < end_time:
        client = random.choice(CLIENTS)

        start_url = f"{BASE_URL}/start/{client}"
        try:
            response = requests.get(start_url)
            print(f"[START] -> {client} | {response.text}")
        except Exception as e:
            print(f"❌ Erro ao iniciar fluxo: {e}")

        if random.random() < END_PROBABILITY:
            time.sleep(random.uniform(0.5, 1.5))  
            end_url = f"{BASE_URL}/end/{client}"
            try:
                response = requests.get(end_url)
                print(f"[END]   -> {client} | {response.text}")
            except Exception as e:
                print(f"❌ Erro ao finalizar fluxo: {e}")

        time.sleep(0.5)

    print("\n✅ Simulação finalizada!")

if __name__ == "__main__":
    simulate()