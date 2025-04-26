__all__ = ['Interpolation']

from dataclasses import dataclass

from .point_set import PointSet
from .polynomial import Polynomial


@dataclass(frozen=True)
class Interpolation:
    points: PointSet
    polynomial: Polynomial
