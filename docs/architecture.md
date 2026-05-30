# GPU Cluster Healthcheck Architecture

## Overview

GPU Cluster Healthcheck is a health validation and observability platform designed for GPU-enabled Kubernetes environments.

The service performs infrastructure validation across:

- NVIDIA GPUs
- NVIDIA Drivers
- CUDA Runtime
- Container Runtime
- Kubernetes Nodes
- GPU Memory Utilization
- MIG Configuration

It exposes:

- REST APIs
- Prometheus Metrics
- Health Scoring
- Alerting Signals

---

## Architecture

                    +----------------+
                    | REST API       |
                    | FastAPI        |
                    +--------+-------+
                             |
                             |
                             v

+--------------------------------------------------+
|                Health Engine                     |
+--------------------------------------------------+

                       Driver Check
                       CUDA Check
                      GPU Inventory
                       Memory Check
                        MIG Check
                      Runtime Check
                     Kubernetes Check

                             |
                             |
                             v

                  +------------------+
                  | Health Scoring   |
                  +--------+---------+
                           |
                           |
                           v

                Cluster Health Score

                           |
        -------------------------------------
        |                                   |
        v                                   v

 Prometheus Exporter               Alert Rules

        |                                   |
        v                                   v

   Prometheus                        AlertManager

        |
        v

    Grafana

---

## Health Scoring Logic

Starting Score: 100

Driver Failure          -20
CUDA Failure            -20
Runtime Failure         -15
Kubernetes Failure      -15
High GPU Memory         -10

Score >= 90
Status = HEALTHY

Score >= 70
Status = WARNING

Score < 70
Status = CRITICAL

---

## Supported Environment

Linux

Kubernetes

NVIDIA GPUs

A100

L40S

Container Runtime

Docker

Prometheus

Grafana