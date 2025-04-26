__all__ = ['FixLenList']

from typing import Generic, TypeVar, Iterable, Iterator

T = TypeVar('T')


class FixLenList(Generic[T]):
    """
    An analog of a list with a fixed length.
    """

    _data: list

    def __init__(self, iterable: Iterable[T]) -> None:
        self._data = list(iterable)

    def __getitem__(self, key: int) -> T:
        return self._data[key]

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self._data})'

    def __setitem__(self, key: int, value: T) -> None:
        self._data[key] = value

    def __str__(self):
        return str(self._data)
