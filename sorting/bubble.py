"""
sorting/bubble.py
Bubble Sort algorithm implementation

High Level Description:
For each element in the list, swap it with its adjacent element until it
is in its correct place. This algorithm doesn't know if the list is already
sorted, so it may go through more passes than necessary.

Time Complexity:
Since the algorithms iterates through every element, this uses O(n) time.
Swapping may take up to O(n/2) time, thus the overall time is O(n^2).
"""


def bubble_sort(lst):
    for i, _ in enumerate(lst):
        for j, _ in enumerate(lst[i:]):
            j += i
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]  # swap
    return lst
