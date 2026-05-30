# Troubleshooting Guide

## Driver Failure

Symptoms:

- nvidia-smi fails
- GPU not visible

Validation:

```bash
nvidia-smi
```

Possible Causes:

- Driver corruption
- Driver mismatch
- GPU hardware issue

Resolution:

- Reinstall NVIDIA driver
- Reboot node
- Validate kernel modules

---

## CUDA Failure

Symptoms:

- CUDA workloads fail
- Runtime initialization errors

Validation:

```bash
nvcc --version
```

Possible Causes:

- Driver/CUDA mismatch
- Broken CUDA installation

Resolution:

- Validate compatibility matrix
- Reinstall CUDA toolkit

---

## High GPU Memory Usage

Symptoms:

- OOM failures
- Inference crashes

Validation:

```bash
nvidia-smi
```

Check:

- Memory Used
- Memory Total

Resolution:

- Reduce model size
- Restart workload
- Allocate additional GPU resources

---

## Kubernetes Node Failure

Symptoms:

- Pods remain Pending
- GPU workloads unscheduled

Validation:

```bash
kubectl get nodes
```

Resolution:

- Verify node status
- Verify kubelet
- Verify device plugin

---

## Device Plugin Failure

Symptoms:

- GPU resources unavailable

Validation:

```bash
kubectl get pods -n kube-system
```

Check:

- nvidia-device-plugin status

Resolution:

- Restart device plugin
- Verify GPU runtime configuration

---

## Metrics Missing

Symptoms:

- Grafana panels empty

Validation:

```bash
curl http://localhost:9100/metrics
```

Resolution:

- Verify exporter process
- Verify Prometheus scrape target