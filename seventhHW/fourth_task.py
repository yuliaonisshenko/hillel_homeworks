"""Implement your own implementation of function max and min (* additional argument amount of result, if you pass 2, function should return 2 max values from the list)"""
from typing import Callable, Iterable, TypeVar, Optional, List

T = TypeVar('T')
def created_max(sequence: Iterable[T], amount: Optional[int] = 1) -> List[T]:
    return sorted(sequence)[-amount:]
def created_min(sequence: Iterable[T], amount: Optional[int] = 1) -> List[T]:
    return sorted(sequence)[:amount]
numbers = [3, 1, 5, 2, 4]
max_value = created_max(numbers)
print(max_value)
min_value = created_min(numbers)
print(min_value)
