import pdb


def mymod(n,m):
    if n > 0:
        while (n > 0):
            n = n - m
        n = n + m

    else:
        while (n < 0):
            n = n + m
    
    return n



if __name__ == '__main__':

    print mymod (13, 5)
    print mymod (-2, 5)
