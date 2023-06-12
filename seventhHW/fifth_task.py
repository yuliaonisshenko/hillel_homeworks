"""Implement your own all function"""
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')

def created_all(sequence: Iterable[T], callback: Callable[[T], bool]) -> bool:
    for item in sequence:
        if not callback(item):
            return False
    return True

def is_positive(x: T) -> bool:
    return x > 0

numbers = [1, 2, 3, 4, 5]
result = created_all(numbers, is_positive)
print(result)
