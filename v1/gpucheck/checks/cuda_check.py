import re

from gpucheck.checks.base import BaseCheck
from gpucheck.models import CheckResult
from gpucheck.collectors.shell import run_command
from gpucheck.constants import CUDA_DRIVER_COMPATIBILITY


class CudaCheck(BaseCheck):

    def run(self):

        nvcc_result = run_command("nvcc --version")

        if nvcc_result["returncode"] != 0:
            return CheckResult(
                name="CUDA Runtime Check",
                status="FAIL",
                severity="CRITICAL",
                message="CUDA runtime unavailable",
                recommendation="Install CUDA toolkit"
            )

        smi_result = run_command("nvidia-smi")

        if smi_result["returncode"] != 0:
            return CheckResult(
                name="CUDA Runtime Check",
                status="FAIL",
                severity="CRITICAL",
                message="Unable to query NVIDIA driver",
                recommendation="Verify NVIDIA driver installation"
            )

        cuda_match = re.search(r"release (\d+\.\d+)", nvcc_result["stdout"])

        driver_match = re.search(
            r"Driver Version:\s+(\d+)",
            smi_result["stdout"]
        )

        if not cuda_match or not driver_match:
            return CheckResult(
                name="CUDA Runtime Check",
                status="WARN",
                severity="MEDIUM",
                message="Unable to determine compatibility"
            )

        cuda_version = cuda_match.group(1)
        driver_version = int(driver_match.group(1))

        required_driver = CUDA_DRIVER_COMPATIBILITY.get(cuda_version)

        if not required_driver:
            return CheckResult(
                name="CUDA Runtime Check",
                status="WARN",
                severity="MEDIUM",
                message=f"Unknown CUDA version {cuda_version}"
            )

        if driver_version < required_driver:
            return CheckResult(
                name="CUDA Runtime Check",
                status="FAIL",
                severity="CRITICAL",
                message=(
                    f"Incompatible driver/runtime. "
                    f"CUDA {cuda_version} requires >= {required_driver}"
                ),
                recommendation="Upgrade NVIDIA driver"
            )

        return CheckResult(
            name="CUDA Runtime Check",
            status="PASS",
            severity="LOW",
            message=(
                f"CUDA {cuda_version} compatible "
                f"with driver {driver_version}"
            )
        )