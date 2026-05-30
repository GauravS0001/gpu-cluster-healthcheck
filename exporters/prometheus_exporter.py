from prometheus_client import Gauge
from prometheus_client import start_http_server

gpu_health = Gauge(
    "gpu_health_status",
    "GPU Health Status"
)

if __name__ == "__main__":

    start_http_server(8000)

    gpu_health.set(1)

    while True:
        pass