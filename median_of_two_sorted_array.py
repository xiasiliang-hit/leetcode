#4. Median of Two Sorted Arrays


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = self.merge(nums1, nums2);
        if len(res) % 2 == 0:
            return (res[len(res)/2 -1] + res[len(res)/2]) /2
        else:
            return (res[len(res)/2])



    def merge(self, nums1, nums2):
        res = []
        i = 0
        j = 0
        while i < len(nums1) and  j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                ++i
            else:
                res.append(nums2[j])
                ++j
                
        if  i==len(nums1):
            while j < len(nums2):
                res.append(nums2[j])
                ++j

        else:
            while i < len(nums1):
                res.append(nums1[i])
                ++i
        print res
        return res

if __name__ == '__main__':
    s = Solution()
    a = [1,2,3]
    b = [6,7,8]
    s.findMedianSortedArray(a, b)
