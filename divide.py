class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if divisor == 0:
            return MAX_INT
        else:
            if abs(dividend) < abs(divisor):
                return 0
            else:
                sign = 1
                if (dividend* divisor<0):
                    sign = -1
                
                d = abs(dividend)
                y = abs(divisor)
                
                
                r = d >> 1
                r2 = y >> 1

                while r2 != 1:
                    r = r >> 1
                    r2 = r2 >> 1
                
                return  t*sign

if __name__ == '__main__':
    s = Solution()
    s.divide()
