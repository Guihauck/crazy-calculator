from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterface(ABC):
    @abstractmethod
    def standard_deviation(self, numbers:List[float]) -> float:
        pass

    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def average(self, numbers: List[float]) -> float:
        pass