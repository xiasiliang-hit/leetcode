class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        pre = nums[0]
        
        i = 1
        l = len(nums)
        while i < l:
            if pre == nums[i]:
                del nums[i]
                l = l -1
            else:
                pre = nums[i]
                i += 1
                
        return
        
