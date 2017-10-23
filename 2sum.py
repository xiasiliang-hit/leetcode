import pdb

class Solution(object):
    def __init__ (self):
        return
    def twosum(self, array, target):
        array.sort()
        for e in array:
            i = array.index(target-e)
            if i != -1 and i != array.index(e):
                return [i, array.index(e)]
            else:
                return 



if __name__ == "__main__":

    array = [range(0, 10)]
    
    s = Solution()
    print s.twosum(array, 8)
