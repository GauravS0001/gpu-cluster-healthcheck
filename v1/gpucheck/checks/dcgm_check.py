import requests

from gpucheck.checks.base import BaseCheck
from gpucheck.models import CheckResult


class DcgmCheck(BaseCheck):

    def run(self):

        try:
            response = requests.get(
                "http://localhost:9400/metrics",
                timeout=3
            )

            if response.status_code != 200:
                return CheckResult(
                    name="DCGM Exporter Check",
                    status="FAIL",
                    message="DCGM metrics endpoint unavailable"
                )

            return CheckResult(
                name="DCGM Exporter Check",
                status="PASS",
                message="DCGM metrics endpoint healthy"
            )

        except Exception:
            return CheckResult(
                name="DCGM Exporter Check",
                status="FAIL",
                message="Unable to connect to DCGM exporter"
            )