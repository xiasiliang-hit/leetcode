class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        mini = sys.maxint
        for i in range(len(strs)):
            if len(strs[i]) < mini:
                mini = len(strs[i])
            else:
                continue
                
        print mini
            
        common = ""
        j = 0
        while j < mini:
            
            flag = True
            
            pre = strs[0][j]
            for k in range(1, len(strs)):
                if strs[k][j] == pre:
                    continue
                else:
                    flag = False # position j does not match
                    break
            
            if flag == False:  # stop here
                break
            
            j+=1
                
        common = strs[0][:j]
            
            
        return common
