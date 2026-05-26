import requests

from gpucheck.checks.base import BaseCheck
from gpucheck.models import CheckResult


class TritonCheck(BaseCheck):

    def run(self):

        try:
            response = requests.get(
                "http://localhost:8000/v2/health/ready",
                timeout=3
            )

            if response.status_code != 200:
                return CheckResult(
                    name="Triton Health Check",
                    status="FAIL",
                    message="Triton not ready"
                )

            return CheckResult(
                name="Triton Health Check",
                status="PASS",
                message="Triton inference server healthy"
            )

        except Exception:
            return CheckResult(
                name="Triton Health Check",
                status="WARN",
                message="Unable to reach Triton endpoint"
            )