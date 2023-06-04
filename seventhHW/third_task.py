"""Implement your own implementation of the function map"""
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def created_map(callback: Callable[[T], U], sequence: Iterable[T]) -> Iterable[U]:
    return (callback(item) for item in sequence)
def square(x: T) -> U:
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = created_map(square, numbers)

for number in squared_numbers:
    print(number)
