""" O(n + m). Could be done in O(log(m + n)) time but it's math heavy and not very interesting.

def median_of_two_sorted_arrays(nums1, nums2)
    i = j = 0
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    mid_index = len(merged) // 2

    print(mid_index)
    print(merged[mid_index])
    print(merged)

    if len(merged) % 2 == 0:
        return (merged[mid_index - 1] + merged[mid_index]) / 2
    else:
        return merged[mid_index]
