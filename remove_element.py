import pdb
import Queue


class Solution(object):
    def removeElement(self, nums, val):

        for i in range(len(nums)):
            ele = nums[i]
            if ele == val:
                del nums[i]
            else:
                continue

        return len(nums)


class MyStack(object):

    def __init__(self) :
        self.que = []
        

    def put(self, val):
        self.que.append(val)
        return True

    def pop(self):
        ele = 0
        n = len(self.que)
        if n != 0:
            ele = self.que[n-1]
            del self.que[n - 1]
        else:
            print "error"
        return ele
    
    def get_len(self):
        return len(self.que)

    
if __name__ == "__main__":

    array = range(0, 100)
    s=MyStack()
    
    s.put(1)
    s.put(5)
    s.put(6)

    print s.pop()
    print s.que
    
    print s.pop()
    print s.que
