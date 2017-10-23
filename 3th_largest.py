import pdb
import random



class Sokution(object):
    def kth_ele(array, k):
        pilot = array[0]

        left = []
        right = []
        
        for ele in array[1:]:
            if ele < pilot:
                left.append(ele)
            elif ele > pilot:
                right.append(ele)
            # pilot is the kth element to be returned
            else:
                return pilot

        if len(left) > k - 1:
            self.kth_ele(left, k)
        elif len(left < k - 1 ):
            self.kth_ele(right, k-len(lef)-1)
        else:
            return pilot

if __name__ == '__main__':
    
    s = Solution
    s.kth_ele(array, 3)

