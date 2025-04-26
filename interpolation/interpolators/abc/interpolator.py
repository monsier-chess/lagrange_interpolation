__all__ = ['ABCInterpolator']

from abc import ABC, abstractmethod

from interpolation import PointSet, Interpolation


class ABCInterpolator(ABC):
    @abstractmethod
    def set_points(self, point_set: PointSet) -> None:
        pass

    @abstractmethod
    def run(self) -> Interpolation | None:
        pass
