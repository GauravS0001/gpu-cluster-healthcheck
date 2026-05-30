# GPU Cluster Healthcheck

GPU Cluster Healthcheck is a GPU infrastructure validation and observability platform designed for Kubernetes-based AI environments.

The project validates GPU readiness, driver health, CUDA availability, container runtime status, Kubernetes node health, and GPU resource utilization.

## Features

- GPU Inventory Discovery
- NVIDIA Driver Validation
- CUDA Runtime Validation
- GPU Memory Monitoring
- MIG Detection
- Kubernetes Node Validation
- Health Scoring Engine
- REST API
- Prometheus Metrics Exporter
- Alert Rules
- Helm Deployment
- Grafana Dashboard

---

## Architecture

Health checks are collected from GPU infrastructure components and aggregated into a cluster health score.

The score is exported to Prometheus and visualized through Grafana dashboards.

---

## API Endpoints

### Health

```bash
GET /health
```

### Cluster Status

```bash
GET /cluster
```

### Metrics

```bash
GET /metrics
```

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start API:

```bash
uvicorn api.server:app --host 0.0.0.0 --port 8000
```

Start exporter:

```bash
python exporter/metrics_exporter.py
```

---

## Example Response

```json
{
  "cluster_score": 92,
  "status": "HEALTHY",
  "issues": []
}
```

---

## Use Cases

- GPU Infrastructure Validation
- Kubernetes GPU Readiness Checks
- AI Inference Environment Health Monitoring
- GPU Capacity Monitoring
- Infrastructure Troubleshooting

---

## Tech Stack

- Python
- FastAPI
- Kubernetes
- NVIDIA GPU Stack
- Prometheus
- Grafana
- Helm