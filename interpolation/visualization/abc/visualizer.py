__all__ = ['ABCVisualizer']

from abc import ABC, abstractmethod

from interpolation import Interpolation


class ABCVisualizer(ABC):
    @abstractmethod
    def set_interpolation(self, interpolation: Interpolation) -> None:
        pass

    @abstractmethod
    def show(self) -> None:
        pass
