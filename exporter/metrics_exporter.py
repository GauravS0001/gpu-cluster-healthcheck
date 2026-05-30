from prometheus_client import Gauge
from prometheus_client import start_http_server

from cmd.healthcheck import run_healthcheck

gpu_health_score = Gauge(
    "gpu_health_score",
    "Overall GPU cluster health score"
)

gpu_driver_status = Gauge(
    "gpu_driver_status",
    "Driver status"
)

gpu_cuda_status = Gauge(
    "gpu_cuda_status",
    "CUDA status"
)

gpu_runtime_status = Gauge(
    "gpu_runtime_status",
    "Container runtime status"
)

gpu_memory_usage_percent = Gauge(
    "gpu_memory_usage_percent",
    "GPU memory usage percentage"
)

gpu_k8s_status = Gauge(
    "gpu_k8s_status",
    "Kubernetes health status"
)


def bool_to_metric(status):

    if status == "healthy":
        return 1

    return 0


def update_metrics():

    result = run_healthcheck()

    results = result["results"]

    score = result["score"]

    gpu_health_score.set(
        score["cluster_score"]
    )

    gpu_driver_status.set(
        bool_to_metric(
            results["driver"]["status"]
        )
    )

    gpu_cuda_status.set(
        bool_to_metric(
            results["cuda"]["status"]
        )
    )

    gpu_runtime_status.set(
        bool_to_metric(
            results["runtime"]["status"]
        )
    )

    gpu_k8s_status.set(
        bool_to_metric(
            results["kubernetes"]["status"]
        )
    )

    gpu_memory_usage_percent.set(
        results["memory"].get(
            "usage_percent",
            0
        )
    )


if __name__ == "__main__":

    start_http_server(9100)

    while True:

        update_metrics()