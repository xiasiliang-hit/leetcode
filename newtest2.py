import pdb


def solution(S):
    max_sum = 0
    current_sum = 0
    positive = False
    n = len(S)
    for i in xrange(n):
#        print 'i---'
#        print i
#        print '---'


#        print max_sum
#        print current_sum
#        print positive
        
#        pdb.set_trace()
        
        item = S[i]
        if item < 0:
            if max_sum < current_sum:
                max_sum += current_sum
                current_sum = item
        else:
            positive = True
            current_sum += item

            
    if (current_sum > max_sum):
        max_sum = current_sum
    if (positive):
        return max_sum
    return -1


if __name__ == "__main__":
    arr =     [-1, 5, -3, 4, 5, -6]
    r = solution(arr)
    print r
    
