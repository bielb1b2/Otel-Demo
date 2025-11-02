# 🌐 Otel Demo

![Java](https://img.shields.io/badge/Java-17-blue)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-green)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![Observability](https://img.shields.io/badge/Observability-OTEL%2FPrometheus%2FGrafana-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Projeto para demonstrar como criar e visualizar métricas utilizando **Micrometer**, **OpenTelemetry**, **Prometheus** e **Grafana**.

---

## ⚙️ Pipeline

O **Micrometer** atua como camada de instrumentação dentro da aplicação, coletando métricas internas (como latência, requisições HTTP, uso de CPU, etc.) e exportando-as via **OTLP (OpenTelemetry Protocol)**.

Essas métricas são enviadas para o **OpenTelemetry Collector**, que funciona como um intermediário: ele recebe, processa e traduz os dados, expondo-os em um formato que o **Prometheus** consegue consumir.

O **Prometheus** realiza a raspagem periódica (*scraping*) dessas métricas e as armazena em sua **time-series database (TSDB)** — um banco otimizado para dados temporais.

Por fim, o **Grafana** se integra ao Prometheus como fonte de dados, permitindo visualizar as métricas em dashboards interativos e configurar alertas, painéis e relatórios em tempo real.


```
[ Micrometer ]
⬇️ (exporta métricas OTLP)

[ OpenTelemetry Collector ]
⬇️ (traduz e expõe em /metrics)

[ Prometheus ]
⬇️ (armazena séries temporais)

[ Grafana ]
⬇️ (visualiza e gera alertas)
```


---

## 📊 Vantagens x Desvantagens

| Abordagem | Vantagens | Desvantagens |
|------------|------------|---------------|
| **Micrometer → OpenTelemetry → Prometheus → Grafana** | ✅ Arquitetura flexível e padronizada (OTLP)<br>✅ Permite unificar métricas, logs e traces<br>✅ Collector pode filtrar e transformar métricas<br>✅ Desacopla aplicação do Prometheus | ❌ Mais complexidade operacional<br>❌ Maior consumo de recursos<br>❌ Curva de aprendizado maior |
| **Micrometer → Prometheus direto** | ✅ Simples de configurar<br>✅ Menos componentes<br>✅ Latência mínima | ❌ Aplicação acoplada ao Prometheus<br>❌ Sem padronização OTLP<br>❌ Dificuldade de integração futura |
| **Micrometer → OpenTelemetry (sem Prometheus)** | ✅ Arquitetura 100% OTLP<br>✅ Integração fácil com backends externos (Grafana Cloud, Datadog, etc.)<br>✅ Sem necessidade de manter Prometheus | ❌ Perde o poder do PromQL e alertas locais<br>❌ Depende de backend externo<br>❌ Menos controle sobre os dados |

---

## 🚀 Tecnologias Utilizadas

- ☕ **Java 17+**
- 🧩 **Micrometer + OpenTelemetry**
- 🐳 **Docker / Docker Compose**
- 📦 **Maven 3.9.9**
- 📊 **Prometheus**
- 📈 **Grafana**

---

## 🏗️ Estrutura do Projeto
```
.
├── 📂 local/
│   └── 🐍 run.py
├── 📂 src/
│   └── 📂 main.java.com.example.otel_demo/
│       ├── controllers/
│       │   └── ☕ FlowController.java
│       └── ☕ OtelDemoApplication.java
├── 🐋 Dockerfile
├── 🐋 Docker-compose.yml
├── 📜 pom.xml
├── 📜 otel-collector-config.yaml
├── 📜 prometheus.yml
└── 📂 target/
```

---

## 🧩 Build & Run

Compile o projeto Java e levante o ambiente de observabilidade:

```bash
mvn clean install
docker-compose up -d
```

### Testando
Dentro da pasta ./local, existe um script Python que simula o fluxo de entrada e saída na aplicação, gerando métricas de teste:

```shell
python local/run.py
```

---

Bielb1b2 
