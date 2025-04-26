__all__ = ['Point']

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterator


@dataclass(frozen=True, order=True)
class Point:
    x: Fraction
    y: Fraction

    def __iter__(self) -> Iterator[Fraction]:
        return iter((self.x, self.y))
