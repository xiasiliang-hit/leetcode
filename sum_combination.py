# does work for 39, one element in candidates can be used multiple times
# not work for 40, do not know where to deduplicate

import pdb

back = []
re = []
    
def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global back
        global re
        candidates = sorted(candidates)
        back = [(target, [], 0)]

        while len(back) != 0:
            ele = back.pop()
            t = ele[0]
            a = ele[1]
            p = ele[2]

            backtrace(candidates, t, a, p)

        return re

#backtrace a single item in back
def backtrace(candidates, target, array, pos):
#    pdb.set_trace()
    global back
    global re

    for i in range(pos, len(candidates)):
            ele = candidates[i]
            aa = list(array)
            print ele
            if target - ele > 0:
                aa.append(ele)
                back.append((target-ele, aa, i+1))

            elif target - ele == 0:
                aa.append(ele)
                re.append( aa )
            else:
                continue
    return 



# leetocde 40
def backtrace2(candidates, target, array, pos):
#    pdb.set_trace()
    global back
    global re

    for i in range(pos, len(candidates)):
#deduplicate but reduce [1,1,6], wrong
#            if i > 0 and candidates[i] == candidates[i-1]:
#                continue
            ele = candidates[i]
            aa = list(array)
            print ele
            if target - ele > 0:
                aa.append(ele)
                back.append((target-ele, aa, i+1)) ### ! pass next position

            elif target - ele == 0:
                aa.append(ele)
                re.append( aa )
            else:
                continue
    return 




if __name__ == "__main__":
    a = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print combinationSum(a, target)                
