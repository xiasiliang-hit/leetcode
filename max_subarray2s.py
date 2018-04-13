# course solution
class Solution(object):
    def maxSubArray(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        d[-1] = (0)
        
        i = 0
        maxi = -sys.maxint
        while i < len(array):
            
            d[i] = d[i-1] + array[i]
            
            if maxi < d[i]:
                maxi = d[i]
            
            if d[i] < 0:
                d[i] = 0
                
            print i
            print d[i]
            

            i+=1
            
        t =   d[len(array) - 1]  
        
        return maxi
