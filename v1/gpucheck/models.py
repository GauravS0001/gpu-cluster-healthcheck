from dataclasses import dataclass
from typing import Optional


@dataclass
class CheckResult:
    name: str
    status: str
    severity: str
    message: str
    recommendation: Optional[str] = None