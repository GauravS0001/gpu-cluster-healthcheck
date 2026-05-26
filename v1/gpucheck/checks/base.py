from abc import ABC, abstractmethod
from gpucheck.models import CheckResult


class BaseCheck(ABC):

    @abstractmethod
    def run(self) -> CheckResult:
        pass