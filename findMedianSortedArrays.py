class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        so = sorted(nums1+nums2)
        
        # linear merge 
        #! append and +, or init, assign and copy, keep behavior consistent
        
        # so = []
        # k = 0
        # i = 0
        # j = 0
        # while (i < len(nums1) and j < len(nums2)):
        #         if nums1[i] < nums2[j]:
        #             so.append (nums1[i]) 
        #             i = i + 1
        #             k = k + 1
                     
        #         else:
        #             so.append(nums2[j])
        #             j = j + 1
        #             k = k + 1
                    
        # if (i == len(nums1)):
        #     so = so + nums2[j:]
        # else:
        #     so = so + nums1[i:]
        
#        print so
        
        length = len(so)
        if length % 2 == 0:
            me = ( so[length/2] + so[length/2 - 1] ) / 2.0
        else:
            me = so[length/2]
            
        return me
