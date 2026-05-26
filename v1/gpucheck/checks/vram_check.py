from gpucheck.checks.base import BaseCheck
from gpucheck.models import CheckResult
from gpucheck.collectors.shell import run_command


class VramCheck(BaseCheck):

    def run(self):

        query = (
            "nvidia-smi "
            "--query-gpu=name,memory.used,memory.total,"
            "temperature.gpu,utilization.gpu,power.draw "
            "--format=csv,noheader,nounits"
        )

        result = run_command(query)

        if result["returncode"] != 0:
            return CheckResult(
                name="VRAM Check",
                status="FAIL",
                severity="HIGH",
                message="Unable to query GPU metrics"
            )

        warnings = []

        for line in result["stdout"].splitlines():

            values = [x.strip() for x in line.split(",")]

            gpu_name = values[0]
            used = int(values[1])
            total = int(values[2])
            temp = int(float(values[3]))
            util = int(values[4])

            usage_percent = (used / total) * 100

            if usage_percent > 90:
                warnings.append(
                    f"{gpu_name}: VRAM usage {usage_percent:.1f}%"
                )

            if temp > 85:
                warnings.append(
                    f"{gpu_name}: GPU temperature critical"
                )

            if util > 98:
                warnings.append(
                    f"{gpu_name}: GPU saturation detected"
                )

        if warnings:
            return CheckResult(
                name="VRAM Check",
                status="WARN",
                severity="HIGH",
                message="; ".join(warnings),
                recommendation="Investigate GPU pressure"
            )

        return CheckResult(
            name="VRAM Check",
            status="PASS",
            severity="LOW",
            message="GPU metrics healthy"
        )