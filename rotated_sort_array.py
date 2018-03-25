# works !

import pdb


def find_pilot(array):
    i = 0
    while i+1 < len(array):
        if array[i] > array[i+1]:
            return array[i+1]
        else:
            continue
        i = i + 1

def find_pilot_devide_conque(array, head, end):
    i = (head+end)/2

    if array[i] > array[end]:
        return find_pilot_devide_conque(array, i+1, end)
    elif array[i] < array[end]:
        return find_pilot_devide_conque(array, head, i)
    else:  #
        return array[i]


if __name__ == "__main__":
    array = [3,4,5,1,2]
    print find_pilot_devide_conque(array, 0, len(array)-1)
#    print find_pilot_devide_conque(array, 0, len(array)-1)        
        
