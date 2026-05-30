from checks.gpu_inventory import get_gpu_inventory
from checks.driver_check import check_driver
from checks.cuda_check import check_cuda
from checks.memory_check import check_memory
from checks.mig_check import check_mig
from checks.runtime_check import check_runtime
from checks.kubernetes_check import check_kubernetes

from scoring.health_score import calculate_score


def run_healthcheck():

    results = {
        "gpu_inventory": get_gpu_inventory(),
        "driver": check_driver(),
        "cuda": check_cuda(),
        "memory": check_memory(),
        "mig": check_mig(),
        "runtime": check_runtime(),
        "kubernetes": check_kubernetes()
    }

    score = calculate_score(results)

    return {
        "results": results,
        "score": score
    }


if __name__ == "__main__":

    output = run_healthcheck()

    print(output)