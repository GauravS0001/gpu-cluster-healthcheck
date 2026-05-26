# GPU Cluster Healthcheck

Production-grade GPU infrastructure diagnostics toolkit for Kubernetes AI inference environments.

`gpu-cluster-healthcheck` helps AI infrastructure engineers validate whether GPU nodes are actually ready for production inference workloads — not just whether `nvidia-smi` works.

The toolkit focuses on operational reliability checks commonly required in:
- Kubernetes GPU clusters
- Triton inference environments
- On-prem AI deployments
- Containerized inference systems
- Production AI serving infrastructure

---

# Why This Exists

Production GPU environments fail in ways that are often difficult to diagnose quickly.

Common examples:
- CUDA runtime mismatch
- GPU visible on host but unavailable inside containers
- Kubernetes device plugin failures
- Broken NVIDIA container runtime
- VRAM pressure causing inference instability
- DCGM exporter failures
- Triton startup failures under GPU memory pressure

Most tooling only validates GPU presence.

This project validates production readiness.

---

# Features

## Current V1 Checks

### NVIDIA Driver Validation
- NVIDIA driver detection
- `nvidia-smi` validation
- NVML accessibility validation

### CUDA Runtime Validation
- CUDA runtime availability
- `nvcc` validation
- Runtime compatibility checks

### Kubernetes GPU Readiness
- GPU allocatable resource validation
- Kubernetes node GPU visibility
- Device plugin readiness verification

### NVIDIA Container Runtime Validation
- NVIDIA runtime detection
- Container GPU runtime sanity checks

### VRAM Health Validation
- GPU memory usage checks
- High memory pressure detection
- VRAM saturation warnings

### DCGM Validation
- DCGM exporter availability
- GPU metrics endpoint validation

### Triton Inference Server Validation
- Triton readiness endpoint validation
- Triton health verification

### Node Pressure Checks
- Early-stage operational sanity validation
- Resource pressure awareness

---

# Architecture

```text
gpu-cluster-healthcheck/
│
├── gpucheck/
│   ├── checks/
│   ├── collectors/
│   ├── utils/
│   └── cli.py
│
├── bash/
├── kubernetes/
├── examples/
└── Dockerfile