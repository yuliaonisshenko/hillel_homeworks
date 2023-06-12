"""Implement your realization of the function filter"""
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')

def created_filter(callback: Callable[[T], bool], sequence: Iterable[T]) -> Iterable[T]:
    return (item for item in sequence if callback(item))
def is_even(x: T) -> bool:
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = created_filter(is_even, numbers)

for number in even_numbers:
    print(number)
