import pdb

def first_missing_pos(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            del(nums[i])
    radix = [None] * len(nums)+1
    for i in range(len(nums)):
       radix[nums[i]] = i

    for j in range(len(radix)):
        if radix[j] == None:
            return j
        else:
            continue
    return len()
