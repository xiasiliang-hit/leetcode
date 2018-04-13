# not pass all cases
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == None:
            return None 
        else:
            pass
        
        intstr = str(x)
        if (x > pow(2,31) - 1) or (x < -pow(2,31)):
            return 0
        else:
            pass
        
        re = ''
        start = 0
        
        if intstr[0] == '-':
            start = 1
            re = "-"
        
        i = len(intstr)-1
        while i >= start:
            re = re + intstr[i]
            i-=1
            
        return int(re)
            
            
if __name__ == "__main__":
    a = [1,1,2,2,3]
    for ele in a:
        if ele == 1:
            del a[a.index(ele)]

    print a
