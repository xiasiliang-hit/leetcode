#5. Longest Palindromic Substring
# time exceeds, O(N2)

# there is Manacher Aglo O(N) 

import os
import pdb

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 1
        result_string = ""
        
        for center in range(0, len(s)):
            center_string = s[center]
            center_max = 1
            offset = 1
            while center - offset >= 0 and center + offset <= len(s) - 1:
                if s[center - offset] == s[center + offset]:
                    center_max = center_max + 2
                    center_string = s[center - offset:center + offset + 1]
                    offset = offset + 1

                else:
                    break
                
            if center_max >= max:
                max = center_max
                result_string = center_string

        for even_left in range(0, len(s)):
            offset = 0
            center_max = 0
            center_string = ""
            
            while even_left - offset >= 0 and even_left + offset + 1 <= len(s) - 1:
                    if s[even_left - offset] == s[even_left + offset + 1]:
                        center_max = center_max + 2
                        center_string = s[even_left - offset : even_left + offset + 2]
                     
                        offset = offset + 1
                    else:
                        break

            if center_max >= max:

                max = center_max         
                result_string = center_string
                    
        return result_string

    def detect_palindrama(self, s):
#        if s % 2  == 0:
            s2 = s
            while s2 != "":
                if s2[0] == s2[-1]:
                    s2 = s2[1:-1]
                else:
                    return False
            return True

#! init "|"
#! iterate center
#! increase interation variable
#! 
    def manacher_algo(self, s):
        newstr = "|"
        for e in s:
            newstr = newstr + (e)
            newstr = newstr + "|"

        maxl = 0
        rstr = ""
        for center in range (0, len(newstr)):
            x = 0
            flag = True
            while (center-x >=0 and center+x <= len(newstr)-1):
                if newstr[center-x] == newstr[center+x]:

                    x = x+1
                    continue
                else:
                    flag = False
                    break

            if maxl < x:
                maxl = x        
                rstr  = newstr[center-x+1:center+x].replace('|', '')
        return rstr

        
            

            
        
                    
if __name__ == "__main__":

    mystr = 'abbb'
    
    solution = Solution()
#    print     solution.longestPalindrome(mystr)


#    print solution.detect_palindrama(mystr)
#    print solution.detect_palindrama("abcbe")
    print solution.manacher_algo(mystr)
