class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        
        re = []
        q = []
        q.append( (target, [])) # put 0 

        while len(q) != 0:
            sol = q.pop()
            if sol[0] == 0:
                re.append(sol[1])
            elif sol[0] < 0:
                pass
            else:
                if sol[1] != []:
                    search_area = list( filter(lambda x : x >= sol[1][-1] , candidates) ) # search only bigger then current elements
                else:
                    search_area = candidates
                    
                for ele in search_area: 
                    q.append( (sol[0] - ele, sol[1] + [ele] ) )
        
        return re 
    

    
