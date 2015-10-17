import factor_decompose as fac
import pdb


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            num = -num
        
        flag = True
#        pdb.set_trace()
                
        l = fac.decompose(num)
        if ( 7 in l or num == 1):
            flag = True
        else:
            flag = False

        return flag


if __name__ == '__main__':
    s = Solution()
    print s.isUgly(1)
            
