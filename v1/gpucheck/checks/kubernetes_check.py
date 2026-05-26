from gpucheck.checks.base import BaseCheck
from gpucheck.models import CheckResult
from gpucheck.collectors.shell import run_command


class KubernetesCheck(BaseCheck):

    def run(self):

        plugin_check = run_command(
            "kubectl get pods -n kube-system | grep nvidia-device-plugin"
        )

        if plugin_check["returncode"] != 0:
            return CheckResult(
                name="Kubernetes GPU Check",
                status="FAIL",
                severity="HIGH",
                message="NVIDIA device plugin not running",
                recommendation="Deploy NVIDIA device plugin"
            )

        allocatable = run_command(
            "kubectl get nodes "
            "-o jsonpath='{.items[*].status.allocatable.nvidia\\.com/gpu}'"
        )

        if allocatable["returncode"] != 0:
            return CheckResult(
                name="Kubernetes GPU Check",
                status="WARN",
                severity="MEDIUM",
                message="Unable to determine allocatable GPUs"
            )

        return CheckResult(
            name="Kubernetes GPU Check",
            status="PASS",
            severity="LOW",
            message=f"Allocatable GPUs: {allocatable['stdout']}"
        )