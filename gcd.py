import pdb
import os
import sys

def gcd(n, m):
    while (n != 0):
        r = m % n
        m = n
        n = r

    return m

if __name__ == '__main__':
    print("input two numbers")
    n1 = (int)(sys.stdin.readline()[:-1])
    n2 = (int)(sys.stdin.readline()[:-1])

#    pdb.set_trace()    
    gcdn = gcd(n1, n2)

    print 'gcd:' + str(gcdn)
