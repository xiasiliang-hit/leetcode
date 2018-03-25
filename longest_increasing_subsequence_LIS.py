# works!

import pdb


#l(s, n) = l(n-1)+s(n), if s(n) > l(n-1)
# or       l(n-1) || l(n-2) + s(n), if l(n-2) < s(n) <= l(n - 1)

# s is string
# n is postion index
temp = []
def LIS(s, n):
    last1 = temp[n-1] #LIS(s[:-1], n-1)
    last2 = temp[n-2]
    
    if s[n] > last1[-1]:
        return last1 + s[n]
    elif s[n] < last1[-1] and s[n] > last2[-1]:
        return last2 + s[n]
    else:
        return last1


def construct(s, n):
    # init
    if len(s) <= 1:
        return s[0:]
    
    if s[0] < s[1]:
        temp.append(s[0])
        temp.append(s[0:2])
    else:
        temp.append(s[0])
        temp.append(s[1])
    
    for i in range(2, len(s)):
        temp.append(  LIS(s, i) )

    return temp[-1]

if __name__ == "__main__":
    s = "1342597"
    print construct(s, len(s) -1)
    
    


