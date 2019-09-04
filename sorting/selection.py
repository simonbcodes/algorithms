"""
sorting/selection.py
Selection sort algorithm implementation

High Level Description:
Continuously takes the minimum value from the list and puts it into its
corresponding position. Repeat until the list is sorted.

Time Complexity:
O(n) for iterating through every element in original array, and O(n/2)
on average for finding the minimum in the rest of the array, thus runtime
is O(n^2)
"""


def selection_sort(lst):
    for i, _ in enumerate(lst):
        min_index = lst.index(min(lst[i:]))
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
