"""
sorting/merge.py

High Level Description:
This sorting algorithm works by repeatedly dividing the given array until each subarray is trivially sorted (length 1). Each subarray is then merged together in order. The merge operation itself is what does the sorting. In the end, we are left with a sorted array.

Time Complexity:
Because the array is being divided into halves, the time taken for division is O(log(n)). The merge operation takes O(n) time, meaning that the overall time complexity is O(nlog(n))
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        i = j = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged


a = [5, 8, 3, 12, 2]
merge_sort(a)
