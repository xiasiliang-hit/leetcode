import pdb

#class Solution(object):
def max_XOR(array):
        comb = get_comb(array)
        remax = max([XOR(couple[0],couple[1]) for couple in comb])

        return remax

#input int
def XOR( a, b):
        abin = "{0:b}".format(a, 2)
        bbin = "{0:b}".format(b, 2)

        (astr,bstr) = makelength(abin, bbin)

        re = ""
        for i in range(0, len(astr)):
            if astr[i] != bstr[i]:  
                re = re + "1" # "1 when diff"
            else:
                re = re + "0" # zero for same
        return int(re, 2)


def makelength(abin, bbin):
        
        if len(abin) > len(bbin):
            dis = len(abin) - len(bbin)
            bbin = "0"*dis + bbin

        else:
            dis = len(bbin) - len(abin)
            abin = "0"*dis + abin
    
        return (abin, bbin)
        

def get_comb(array):
        re = []
        for e1 in array:
            for i in range(array.index(e1), len(array)):
                e2 = array[i]
                re.append([e1,e2])

        return re


if __name__ == '__main__':

        a = [3, 10, 5, 25, 2, 8]
        print max_XOR(a)

    

