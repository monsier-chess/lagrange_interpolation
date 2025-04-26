__all__ = ['PointSet']

from fractions import Fraction
from typing import Iterable, Iterator

from .point import Point


class PointSet:
    def __init__(self, points: Iterable[Point]) -> None:
        unique_x: set[Fraction] = set()
        unique_points: set[Point] = set()
        for point in points:
            x, y = point
            if x in unique_x:
                continue
            unique_x.add(x)
            unique_points.add(point)
        self._points = unique_points

    def __len__(self):
        return len(self._points)

    def __iter__(self) -> Iterator:
        return iter(self._points)
