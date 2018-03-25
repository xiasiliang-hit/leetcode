#permutaion  arrays 
def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        
        first = nums[0]
        last = permute(nums[1:])
        re = []
        for ele in last:
            for i in range(0, len(ele) + 1):
                if i == 0:
                    head = []
                else:
                    head = ele[0:i]

#                print head

                head.append(first)
                head.extend( ele[i:] )

                re.append(head)

        return re
            
if __name__ == "__main__":
    nums = [1, 2,3]
    print permute(nums)        
