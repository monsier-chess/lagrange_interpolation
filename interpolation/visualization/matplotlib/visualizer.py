__all__ = ['MatplotlibVisualizer']

from typing_extensions import override
from fractions import Fraction
import matplotlib.pyplot as plt

from interpolation import Interpolation
from interpolation.visualization import ABCVisualizer


class MatplotlibVisualizer(ABCVisualizer):
    def __init__(self, polynomial_dots: int = 100, pad_x: Fraction = Fraction(10)):
        self._polynomial_dots = polynomial_dots
        self._pad_x = pad_x
        self._interpolation: Interpolation | None = None

    @override
    def set_interpolation(self, interpolation: Interpolation) -> None:
        self._interpolation = interpolation

    @override
    def show(self) -> None:
        points = sorted(self._interpolation.points)
        x_list, y_list = zip(*points)
        start_x = x_list[0] - self._pad_x
        end_x = x_list[-1] + self._pad_x
        step = (end_x - start_x) / (self._polynomial_dots - 1)
        plot_x_list = [step * i for i in range(self._polynomial_dots)]
        plot_y_list = list(map(self._interpolation.polynomial, plot_x_list))
        plt.plot(plot_x_list, plot_y_list)
        plt.scatter(x_list, y_list)
        plt.show()
