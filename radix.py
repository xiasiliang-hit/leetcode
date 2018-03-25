def radix_sort(array):
    l = len(array)
    re = [0]* l
    for e in array:

            re[e] = re[e] + 1


    j = 0
    result = [0]*l
    for i in range(l):
#        if re[i] != None:
            count = re[i]
            k = 0
            while k < count:
                result[j] = i
                j = j+1
                k = k+1

    return result
if __name__ == "__main__":
    array=[1,2,1,2,5,3,4,4,3]
    print radix_sort(array)                
            
