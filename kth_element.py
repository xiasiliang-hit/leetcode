import pdb
import random


def kth_element(narray, k):
    #newn = [None] + n
    target = narray[0]

    left = []
    right = []
    
    for ele in narray[1:]:
        if (ele < target):
            left.append(ele)            
        elif (ele > target):
            right.append(ele)
        else:
            continue
    
    if (len(left) > k-1):
        return kth_element(left, k-1)
    elif (len(left) < k-1):
        return kth_element(right, k-len(left)-1)
    else:
        return target 

if __name__ == "__main__":
    array = range(0, 100)+[49]
    random.shuffle(array)
    print array
    print kth_element(array, 50)

