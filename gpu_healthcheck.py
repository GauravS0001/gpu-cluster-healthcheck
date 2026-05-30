import argparse

from checks.gpu_inventory import get_gpu_inventory
from checks.driver_check import check_driver
from checks.cuda_check import check_cuda
from checks.runtime_check import check_container_runtime
from checks.kubernetes_check import check_nodes
from checks.device_plugin_check import check_device_plugin

from reports.report_generator import generate_report


def scan():

    results = {
        "gpu_inventory": get_gpu_inventory(),
        "driver": check_driver(),
        "cuda": check_cuda(),
        "runtime": check_container_runtime(),
        "nodes": check_nodes(),
        "device_plugin": check_device_plugin()
    }

    generate_report(results)

    print("Health scan completed")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        choices=["scan", "report", "validate"]
    )

    args = parser.parse_args()

    if args.command == "scan":
        scan()

    elif args.command == "validate":
        scan()

    elif args.command == "report":
        print("reports/health-report.txt")