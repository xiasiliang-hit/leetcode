# time exceed

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        m = {}
        
        re = {}
        for ele in strs:
            flag = False
            
            for anakey in m.keys():
                anas = m[anakey]
                if ele in anas:
                    re[anakey].append(ele)
                    #strs.remove(ele)
                    flag = True
                    break
                    
            if flag == False:
                    m[ele] = permutation2(ele)
                    re[ele] = [ele]
         

        result = []
        for key in re.keys():
            result.append(re[key])

        return result
                
        
        
        
def permutation2(mystr):
#    global ix
#    ix = ix+1

    if len(mystr) <= 1:
        return mystr
    
    res = []
    for i in range(len(mystr)):
        mys = mystr
        ele = mys[i]
        permutations = permutation2(mys[:i] + mys[i+1:])
        for permutation in permutations:

            res.append(ele + permutation)        
    return res 
