import pdb

def bubble_sort(li):
    j = len(li) - 1

    while j >= 1:
        i = 0
        while i < j :
            if li[i] > li [i+1]:
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp
#            else:
#                continue

            i = i+1
        j = j -1
    return li


if __name__ == '__main__':
    print 'in main'
    
    a = [5,4,3,1,2]
    re = bubble_sort(a)
    print 'a'
    print a
    print 're'
    print re
