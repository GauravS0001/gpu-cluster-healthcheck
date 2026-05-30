# GPU Cluster Healthcheck Runbook

## Service Health Validation

Validate service startup:

```bash
curl http://localhost:8000/health
```

Expected:

```json
{
  "cluster_score": 100,
  "status": "HEALTHY"
}
```

---

## Validate GPU Visibility

Run:

```bash
nvidia-smi
```

Expected:

- GPU visible
- Driver loaded
- Memory information available

Failure Symptoms:

- No devices found
- Driver communication failure

---

## Validate CUDA Runtime

Run:

```bash
nvcc --version
```

Expected:

CUDA version returned successfully.

Failure Symptoms:

- nvcc not found
- CUDA mismatch

---

## Validate Container Runtime

Run:

```bash
docker info
```

Expected:

Container runtime available.

Failure Symptoms:

- Docker daemon unavailable
- Runtime startup failure

---

## Validate Kubernetes Nodes

Run:

```bash
kubectl get nodes
```

Expected:

All nodes in Ready state.

Failure Symptoms:

- NodeNotReady
- Scheduling disabled
- Resource pressure

---

## Validate Metrics Endpoint

Run:

```bash
curl http://localhost:9100/metrics
```

Expected:

Prometheus metrics visible.

---

## Validate Alert Rules

Check Prometheus:

```bash
http://prometheus:9090/rules
```

Expected:

All GPU health rules loaded successfully.