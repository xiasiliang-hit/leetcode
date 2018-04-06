class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        ini = [[0], [1]]
        for i in range(len(nums)-1):
            ini = self.mult(ini)        

        re = []
        for ele in ini:
            bitvector = []
            for i in range(len(ele)):
                x = int(nums[i]) * ele[i]
                if x != 0:
                    bitvector.append(x)
            re.append(bitvector)

        return re
                
    def mult(self, array):
        re = []
        for ele in array:
            re.append(ele + [0])
            re.append(ele+ [1])
        return re


if __name__ == '__main__':
    s = Solution()
    print s.subsets("123")
