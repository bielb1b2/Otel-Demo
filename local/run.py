import random
import time
import uuid
import requests

CLIENTS = ["Sao Paulo", "Salvador", "Rio de Janeiro", "Santa Catarina", "Belo Horizonte"]
BASE_URL = "http://localhost:8080/flow"
RUN_DURATION = 60 * 2  # 2 minutos
END_PROBABILITY = 0.7

def generate_traceparent(trace_id=None):
    if trace_id is None:
        trace_id = uuid.uuid4().hex  
    span_id = uuid.uuid4().hex[:16]
    return trace_id, f"00-{trace_id}-{span_id}-01"

def simulate():
    end_time = time.time() + RUN_DURATION
    print(f"🚀 Iniciando simulação one-shot de fluxos por {RUN_DURATION} segundos...\n")

    while time.time() < end_time:
        client = random.choice(CLIENTS)

        # Cria um novo trace (one-shot)
        trace_id, traceparent_start = generate_traceparent()
        headers = {"traceparent": traceparent_start}

        # 🔹 1. Envia o START
        start_url = f"{BASE_URL}/start/{client}"
        try:
            requests.get(start_url, headers=headers)
            print(f"[TRACE START] client={client} trace_id={trace_id}")
        except Exception as e:
            print(f"❌ Erro ao iniciar fluxo: {e}")
            continue

        # 🔹 2. Com probabilidade, envia o END
        if random.random() < END_PROBABILITY:
            time.sleep(random.uniform(0.3, 1.2))
            _, traceparent_end = generate_traceparent(trace_id)
            end_headers = {"traceparent": traceparent_end}
            end_url = f"{BASE_URL}/end/{client}"

            try:
                requests.get(end_url, headers=end_headers)
                print(f"[TRACE END]   client={client} trace_id={trace_id}")
            except Exception as e:
                print(f"❌ Erro ao finalizar fluxo: {e}")
        else:
            print(f"⚠️ Fluxo {client} não foi finalizado (trace incompleto)")

        time.sleep(random.uniform(0.4, 1.0))

    print("\n✅ Simulação finalizada!")


if __name__ == "__main__":
    simulate()
