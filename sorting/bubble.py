"""
sorting/bubble.py
Bubble Sort algorithm implementation
O(n^2)
"""


def bubble_sort(arr):
    for i, _ in enumerate(arr):
        for j, _ in enumerate(arr[i:]):
            j += i
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]  # swap
    return arr
