import sys
import pdb
import pdb
import math

def decompose(num):
       
        r = num
        factor = []

        while (r != 1):
#            pdb.set_trace()

            flag = False
            for i in range(2, (int)(math.ceil(math.sqrt(r)))):
                if r % i == 0:
                    r = (int)(r/i)
                    factor.append(i)
                    flag = True
                    break
                else:
                    continue

            if flag == False:  # r is prime
                factor.append(r)
                break

        return factor


    
if __name__ == '__main__':            
    l = decompose(35)
    print l
    
