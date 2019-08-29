import pytest

from bubble import bubble_sort


@pytest.mark.parametrize('to_sort', [
    ([]),
    ([5, 4, 3, 2, 1]),
    ([1, 2, 3, 4, 5]),
    ([0])
])
def test_bubble_sort(to_sort):
    assert bubble_sort(to_sort) == sorted(to_sort)
