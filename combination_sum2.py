#lc 40

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        
        re = []
        q = []
        q.append( (target, [], -1)) # put 0 

        while len(q) != 0:
            
            sol = q.pop()
            if sol[0] == 0:
                re.append(sol[1])
            elif sol[0] < 0:
                pass
            else:
                #if sol[1] != [] and sol[2]+1 < len(candidates):
                #    search_area = candidates[sol[2]+1:]  # search only bigger then current elements
                #else:
                #    search_area = candidates
                
                pre  = 0
                for i in range(len(candidates)):
                    ele = candidates[i]
                    if i <= sol[2]: # use only once, reduce [2,2,2,2]
                        continue
                    if ele == pre: # deduplicate [1,7]
                        continue
                    
                    q.append( (sol[0] - ele, sol[1] + [ele], i ) )
                    
                    pre = ele
        
        return re 
    

##
# [10,1,2,7,6,1,5]
# 8
