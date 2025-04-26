from fractions import Fraction
from interpolation import (
    Point,
    PointSet,
    Lagrange,
    MatplotlibVisualizer,
    Interpolation,
)


def main() -> None:
    points = PointSet(
        [
            Point(Fraction(10), Fraction(20)),
            Point(Fraction(20), Fraction(15)),
            Point(Fraction(30), Fraction(30)),
        ]
    )
    lagrange = Lagrange()
    lagrange.set_points(points)
    interpolation_info: Interpolation | None = lagrange.run()
    visualizer = MatplotlibVisualizer()
    visualizer.set_interpolation(interpolation_info)
    visualizer.show()


if __name__ == '__main__':
    main()
