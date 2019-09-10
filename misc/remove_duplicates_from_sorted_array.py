# remove duplicates in place from a given list O(n)

def remove_duplicates(nums):
    ix = 1  
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[ix] = nums[i]
            ix += 1
    del nums[ix:]

lst = [1, 1, 2]
remove_duplicates(lst)
print(lst)
