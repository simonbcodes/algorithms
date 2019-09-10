# find single occurence of number in array, O(n) with O(n) space

def single_number(nums):
    hsh = {}
    for n in nums:
        if n in hsh and hsh[n] == 1:
            del hsh[n]
        else:
            hsh[n] = 1
    for i, val in hsh.items():
        return i
