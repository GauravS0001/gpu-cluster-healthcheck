from gpucheck.checks.base import BaseCheck
from gpucheck.models import CheckResult
from gpucheck.collectors.shell import run_command


class RuntimeCheck(BaseCheck):

    def run(self):

        result = run_command("docker info | grep nvidia")

        if result["returncode"] != 0:
            return CheckResult(
                name="Container Runtime Check",
                status="WARN",
                message="NVIDIA container runtime not detected",
                recommendation="Install NVIDIA container toolkit"
            )

        return CheckResult(
            name="Container Runtime Check",
            status="PASS",
            message="NVIDIA runtime available"
        )