import itertools
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar('T')
def sliding_window[T](iterable: Iterable[T], n: int):
    iterables = itertools.tee(iterable, n)
    
    for it, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            _ = next(it, None)
    
    return zip(*iterables)

