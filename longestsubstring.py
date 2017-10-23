# use sliding window
import pdb

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = [None] * 200
        head = 0
        end = 0
        maxlength = 0
        
        for i in range(0, len(s)):

            #if s[i] == 'b':
            #    pdb.set_trace()
                
            aChar = s[i]
            end = i
        
            
        
            if hashtable[ord(aChar)] != None:
                head = hashtable[ord(aChar)] + 1

            # !! coutn max when for last char in sequence that does not exist in hash table  
            else:
                if (end - head + 1 > maxlength):
                    maxlength = end - head + 1

            
            hashtable[ord(aChar)] = i

        return maxlength


if __name__ == '__main__':

    print 'main'
    s = "tmmzuxt"
    solution = Solution()
    
    LLS = solution.lengthOfLongestSubstring(s)
    print LLS
