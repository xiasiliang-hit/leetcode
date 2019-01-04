# time exceeds

import math

def uglyNumber(num):
    re = []
    i = 2
    
    if num == 1:
        return True
    if num < 0:
        return False
    
    while i <= math.sqrt(num):
        if num % i == 0:
          re.append(i)
          num = num / i
          
        else:
          i+=1
          continue

    re.append(num)

    flag = True
    for factor in re:
        if factor not in [2,3,5]:
            return False
        else:
            continue

    return flag
            

def nthUglyNumber(n):
    i = 0
    e = 1
    
    while True:
        if uglyNumber(e):
          i += 1

        if i == n:
            return e
        e += 1
        
    return None

if __name__ == "__main__":
    
    print nthUglyNumber(172)
