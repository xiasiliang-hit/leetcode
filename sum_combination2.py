back = []
re = []
candidates = []

def init(c, t):
    candidates = c
    back.append((t,[]))
    re = []


def combinationSum(candidates, target, part_solution_arr, pos):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        while len(back) != 0:
            ele = back.pop()
            t = ele[0]
            a = ele[1]
            p = ele[2]
            
            for i in range(pos, len(candidates)):
                if target - ele > 0:
                    part_solution_arr.append(ele)
                    back.append((target-ele, part_solution_arr, i))

                elif target - ele == 0:
                    part_solution_arr.append(ele)
                    re.append( part_solution_arr )
                else:
                    pass

            combinationSum(candidates, t, a, p)
                
        return re


if __name__ == "__main__":
    candidates = [2,3,4,7]
    target = 7
    array = []

    init(candidates, target)
    print combinationSum(candidates, target, array, 0)
            
