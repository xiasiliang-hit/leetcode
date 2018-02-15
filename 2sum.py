import pdb

class Solution(object):
    def __init__ (self):
        return


    #sorted and search
    #can not return index
    # return only one pair
    def twosum(self, array, target):
        array.sort()
        for i in range(0, len(array)):
            B = target - array[i]
            iB = array.find(B)
            if in != -1 and in != array.index(i):
                return [array[i], array[iB]]
            else:
                continue

    # hash
    # can return index or element
    # return multiple pairs
    def twosum_(self, nums, target):
        re = []
        d = {}
        for i in range(0, len(nums)):
            B = target - nums[i]
            if nums[i] in d.keys() and B in d.keys():
                iB = d[B]
                del d[B]
                del d[nums[i]]
                re.append([i, iB])
            else:
                continue

    #sort poiter
    def two_sum_pointer

if __name__ == "__main__":

    array = [range(0, 10)]
    
    s = Solution()
    print s.twosum(array, 8)
