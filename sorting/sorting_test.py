import random

import pytest

from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort

algorithms = [bubble_sort, selection_sort, insertion_sort]

test_list = list(range(0, 101))


@pytest.mark.parametrize('to_sort', [
    ([]),
    ([5, 4, 3, 2, 1]),
    ([1, 2, 3, 4, 5]),
    (random.sample(test_list, 10)),
    (random.sample(test_list, 10)),
    (random.sample(test_list, 10)),
    ([0])
])
def test_sort(to_sort):
    for algo in algorithms:
        print(algo.__name__)
        assert algo(to_sort) == sorted(to_sort)
