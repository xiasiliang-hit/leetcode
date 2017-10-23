import pdb
import math


def solution(S):
    max_sum = 0
    current_sum = 0


    for i in range(0,len(S)):
        #print 'i---'
        #print i
#        pdb.set_trace()
        if current_sum > 0:
            max_sum = max_sum + current_sum
            current_sum = S[i]
        else:
            current_sum = current_sum + S[i]


    result = max_sum
    current_sum = 0

    for i in range(0, len(S)):
        if current_sum < 0:
            result = result - current_sum
            current_sum = S[i]
        else:
            current_sum = current_sum + S[i]
        
    return result


if __name__ == '__main__':
    arr = [1, 2, -3, 4, 5, -6]
    r = solution(arr)
    print r
