

# solved
# return [index1, index2]
#! index should be diff
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):     #! index from i+1
                if nums[i] + nums[j] == target:
                    return [i, j]


# use hashset
#! two sum and return one pair of index
#! for an element there is at most one ther other match 
# if there are, need reduce, 
    def twoSum(self, nums, target):
        d = {}
        for i in range(0,  len( nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = i
            else:
                #d[nums[i]].append(i)                
                continue

        for i in range(0, len( nums)):
            ele = nums[i]
            t = target - ele
            if t in d.keys() and d[t] != i:

                return [i, d[t]]
            else:
                continue

    
if __name__ == '__main__':

    
