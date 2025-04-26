__all__ = ['Lagrange']

from fractions import Fraction
from typing_extensions import override

from interpolation import PointSet, Polynomial, Interpolation
from interpolation.interpolators import ABCInterpolator


class Lagrange(ABCInterpolator):
    def __init__(self) -> None:
        self._points: PointSet | None = None
        self._polygon: Polynomial | None = None

    @override
    def set_points(self, point_set: PointSet) -> None:
        self._points = point_set

    @override
    def run(self) -> Interpolation | None:
        if self._points is None:
            return
        polynomial = Polynomial(0)
        x = Polynomial(1, [Fraction(0), Fraction(1)])
        x_list, y_list = zip(*self._points)
        for i in range(len(self._points)):
            base_polynomial = Polynomial(0, [Fraction(1)])
            for j in range(len(self._points)):
                if i == j:
                    continue
                base_polynomial *= (x - x_list[j]) * (
                    Fraction(1) / (x_list[i] - x_list[j])
                )
            base_polynomial *= y_list[i]
            polynomial += base_polynomial
        return Interpolation(points=self._points, polynomial=polynomial)
