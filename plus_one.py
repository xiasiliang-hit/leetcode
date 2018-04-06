# not working
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == None:
            return 1
        
        digits2 = [0] + digits
        
        
        i = len(digits2)-1
        sums = 1
        while i >=0:
            c = digits2[i]
            sums = c+sums
            digits2[i] = sums[-1]
            
            if len(sums) == 2:
                sums = 1
            else:
                sums = 0
                
            i += 1
            
        
        return digits2 
            
            
        
