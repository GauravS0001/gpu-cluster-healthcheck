from gpucheck.checks.base import BaseCheck
from gpucheck.models import CheckResult
from gpucheck.collectors.shell import run_command


class DriverCheck(BaseCheck):

    def run(self):

        result = run_command("nvidia-smi")

        if result["returncode"] != 0:
            return CheckResult(
                name="NVIDIA Driver Check",
                status="FAIL",
                message="nvidia-smi failed",
                recommendation="Verify NVIDIA drivers and kernel modules"
            )

        return CheckResult(
            name="NVIDIA Driver Check",
            status="PASS",
            message="NVIDIA driver operational"
        )