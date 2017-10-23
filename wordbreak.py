import pdb

#f(i) = true  when {for any 0<j<i if f(j)=true and s[j+1, i]}

class Solution(object):

    #using split
        def wordBreak(self, s, wordDict):
                flag = [False]*(len(s)+1)
                flag[0] = True # means split
                for i in range(1, len(s)+1): # split
                    for j in range(0, i): # iterator of split
                        if flag[j] and s[j:i] in wordDict:
                            flag[i] = True
                        else:
                            continue
                        
                    print flag
                    
                return flag[len(s)]

    #use str index
        def wordBreak2(self, s, wordDict):
            flag = [False]*len(s)

            if s[0] in wordDict:
                flag[0] = True
            #else do nothing

            for i in range(1, len(s)):
                if s[:i+1] in wordDict:
                    flag[i] = True
                
                for j in range(0, i):
                    if (flag[j] and s[j+1:i+1] in wordDict):
                        flag[i] = True

                
                print flag
            return flag[len(s)-1]
            
#                return flag[len(s)]

if __name__ == "__main__":
    s = Solution()
    print s.wordBreak2("abcda", ["a", "b", "cd"])

