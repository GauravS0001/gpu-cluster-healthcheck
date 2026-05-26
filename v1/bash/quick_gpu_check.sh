#!/bin/bash

echo "========== NVIDIA SMI =========="
nvidia-smi

echo "========== CUDA VERSION =========="
nvcc --version

echo "========== DOCKER RUNTIME =========="
docker info | grep nvidia