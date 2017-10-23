import pdb
import headq
import math

def get_median(array): # assume len is greater than
    small = array[0] < array[1] ? array[0] : array[1]
    big = array[0] < array[1] ? array[1] : array[0]
    
    median = (small + big ) /2.0
    print array[0], median 

    headL = []
    headright = []

    headppush(headright, big)
    headppush(headL, small) 
    
    for e in array[2:]:
        if e > median:
            headppush(headright, median)

            if len(headL) == len(headright):
                median = (headL[0] + headright[0])/2
                print median,

            elif len(headL) + 1 = len(headright):
                median = headright[0]
                print median,

            elif len(headL) + 2 = len(headright):
                balance(headright, headL)
                median = (headL[0] + headright[0])/2
                print median

            else:
                print "error"

        else:
            
                
def balance(a, b):
    if ((len(a) - len(b)) == 2):
        headqpush(b, a.pop())
    else:
        headqpush(a, b.pop())
    return 
        
                
if __name__ == "__main__":
    a= [2,1,3,4,5,6]
    get_median()                
                



