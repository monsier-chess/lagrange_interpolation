__all__ = ['Polynomial']

from fractions import Fraction
from typing import Iterable, Self

from .structures import FixLenList


class Polynomial:
    """
    Polynomial class with fraction coefficients, written in little indian.
    Immutable. Adds zeros in higher powers if necessary.
    """

    _degree: int
    _coefficients: FixLenList[Fraction]

    def __init__(
        self,
        degree: int,
        coefficients: Iterable[Fraction] | None = None,
    ) -> None:
        if coefficients is None:
            coefficients = []
        coefficients: list[Fraction] = list(coefficients)
        if degree < 0:
            raise ValueError(
                f'Polynomial degree cannot be negative, but {degree} is given'
            )
        if len(coefficients) > degree + 1:
            raise ValueError(
                f'Too many coefficients ({len(coefficients)}) '
                f'are given for the polynomial of this degree ({degree})'
            )
        zeroes = [Fraction(0)] * (degree + 1 - len(coefficients))
        coefficients = coefficients + zeroes
        self._coefficients = FixLenList(coefficients)
        self._degree = degree

    def __add__(self, other: 'Polynomial | Fraction') -> Self:
        return self.add(other)

    def __call__(self, value: Fraction):
        result = self.coefficients[0]
        x_power_i = value
        for i in range(1, len(self.coefficients)):
            result += self.coefficients[i] * x_power_i
            x_power_i *= value
        return result

    def __mul__(self, other: 'Polynomial | Fraction') -> Self:
        return self.mul(other)

    def __sub__(self, other: 'Polynomial | Fraction') -> Self:
        return self.sub(other)

    def __neg__(self) -> 'Polynomial':
        return self * Fraction(-1)

    @property
    def degree(self) -> int:
        return self._degree

    @property
    def coefficients(self) -> FixLenList:
        return self._coefficients

    def sub(
        self,
        other: 'Polynomial | Fraction',
        minimize: bool = True,
    ) -> Self:
        negative = -other
        return self.add(negative, minimize)

    def add(
        self,
        other: 'Polynomial | Fraction',
        minimize: bool = True,
    ) -> Self:
        if isinstance(other, Fraction):
            other: Polynomial = type(self)(0, [other])

        min_degree = self.degree if self.degree < other.degree else other.degree
        sep_index = min_degree + 1
        self_coefficients = list(self.coefficients)
        other_coefficients = list(other.coefficients)
        self_prefix, self_suffix = (
            self_coefficients[:sep_index],
            self_coefficients[sep_index:],
        )
        other_prefix, other_suffix = (
            other_coefficients[:sep_index],
            other_coefficients[sep_index:],
        )
        suffix = self_suffix or other_suffix
        coefficients: list[Fraction] = []
        for first, second in zip(self_prefix, other_prefix):
            coefficients.append(first + second)
        coefficients.extend(suffix)
        polynomial = type(self)(len(coefficients) - 1, coefficients)
        if minimize:
            polynomial = polynomial.minimize_degree()
        return polynomial

    def mul(
        self,
        other: 'Polynomial | Fraction',
        minimize: bool = True,
    ) -> Self:
        degree: int | None = None
        coefficients: list[Fraction] | FixLenList[Fraction] | None = None
        if isinstance(other, Polynomial):
            degree = self.degree + other.degree
            coefficients = [Fraction(0)] * (degree + 1)
            for i, self_coeff_i in enumerate(self.coefficients):
                for j, other_coeff_j in enumerate(other.coefficients):
                    coefficients[i + j] += self_coeff_i * other_coeff_j
        elif isinstance(other, Fraction):
            degree = self.degree
            coefficients = self.coefficients
            for i in range(len(self.coefficients)):
                self.coefficients[i] *= other
        else:
            raise NotImplementedError
        polynomial = type(self)(degree, coefficients)
        if minimize:
            polynomial = polynomial.minimize_degree()
        return polynomial

    def minimize_degree(self) -> Self:
        zero = Fraction(0)
        coefficients = list(self.coefficients)
        min_degree = 0
        for index in reversed(range(len(self.coefficients))):
            if coefficients[index] == zero:
                continue
            min_degree = index
            break
        coefficients = coefficients[: min_degree + 1]
        min_polynomial = type(self)(min_degree, coefficients)
        return min_polynomial
