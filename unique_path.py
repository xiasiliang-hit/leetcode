# lc 62
# calculate the result

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n<= 1 or m<=1:
            return 1
        
        a = n-1
        b = m-1
        t = a + b
        
        return self.factorial(t) / self.factorial(a) / self.factorial(b) 
        
    def factorial(self, x):
        if x == 1:
            return 1
        else:
            return x*self.factorial(x-1)
