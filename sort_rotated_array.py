# max depth of recursion 

import pdb

def func(array,target):

    if array == []:
        return None
    
    pos = find_split(array, 0, len(array)-1)

    if target == array[0]:
        return 0
    
    if target > array[0]:
        return find_target(array, target, 0, pos)

    else:
        return find_target(array, target,  pos +1, len(array)-1)
        
#    return find_target(array, target, 0, len(array)-1, pos)


def find_target(array,target, s, end):
    if target == array[s]:
        return s
    
    elif target < array[s]:
        return find_target(array, target, s, (s+end) / 2)
    else:
        return find_target(array, target, (s+end) / 2, end)

    
def find_split(array, s, end ):
    l = len(array)
    p = (s+end) / 2

    if array[s] > array[s+1]:
        return s
    
    if array[p] > array[l-1]:
        return find_split(array, p, end )
    else:
        return find_split(array, s, p)
    

if __name__ == "__main__":
    
    arra = [4,5,6,7,1,2,3]
    print func(arra,2)

    
