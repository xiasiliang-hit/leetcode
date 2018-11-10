import sys
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
        start = -1
        end = 0
        while i < len(array):
            
            d[i] = d[i-1] + array[i]
            
            if maxi < d[i]:
                maxi = d[i]
                end = i
                
            if d[i] < 0:
                d[i] = 0
                start = i

            i+=1
        
        return maxi


# dp: this works 
    def max_test(self, arrray ):
        i = 0
        maxi = 0
        start = 0
        end = 0
        m = [0]* len(array)
        
        while i <= len(array)-1:
            if (m[i-1]+array[i] >  array[i]):
                m[i] = m[i-1]+array[i]
                end = i
            else:
                m[i] = array[i]
                start = i

            if maxi < m[i]:
                maxi = m[i]
                
            i = i+1
        print m
        return maxi, start, end

# simple brute force O(n2)
    def max_brute(self,array):
        d = [0]*len(array)
        
        maxi = 0
        for i in range(0, len(array)):
            d[i] = d[i-1] + array[i] # d[i-1] == 0

        for j in range(0, len(d)):
            for k in range(j+1, len(d)):
                print maxi
                if maxi < d[k] - d[j]:
                    maxi = d[k] - d[j]
        print d
        return maxi
                

        


    
def max(a, b):
    if a > b:
        return a
    else:
        return b

def maxinarray(array):
    maxim = 0
    for i in range(0, len(array)):
        if maxim < array[i] :
            maxim = array[i]
    return maxim





        
if __name__ == "__main__":
    s = Solution()
    
    array = [-2,-3]
    print "array:", array
    print "subarray:", s.maxSubArray(array)        

    array = [-2,-1]
    print "array", array
    print "subarray:", s.maxSubArray(array)

    array = [3,5,1, -20, 4,5,6]
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#    print "array", array
    print "subarray:", s.max_brute(array)
