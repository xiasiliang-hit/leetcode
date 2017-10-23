import pdb
import os


def quick_sort(array):
    pilot = array[0]

    i = 0
    j = len(array)-1
    

    return result


def sort(start, end, array):
    if start >= end:
        return
    else:
        i = start
        j = end

        pilot = array[i]
        ele = array[i+1]
        
        while i < j:
            if ele < pilot:
                array[i] = ele
                i = i + 1
            else:
                ele = 0
                array[j] = pilot
                j = j - 1

def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if (x >= pow(2,32) or x <= -pow(2,32)):
            return 0

        else:
            if x < 0:
                sign = "-"
            else:
                sign = ""
                
            newstr = ""
            s = str(abs(x))
#            print s
            i = len(s)-1
            while i >= 0:
                newstr = newstr + s[i]
                i = i - 1

            
            newx = int(sign+newstr)

        return newx
    
if __name__ == '__main__':
    test_arr = [1,3,9]
#    print square(test_arr)

    test_arr = [0,-1,2]
#    print square(test_arr)


    print reverse(-12345)
