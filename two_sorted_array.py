import pdb


# assume a1 and a2 are sorted
def merge_sort(a1, a2):
        i = 0
        j = 0
        re = [None] * (len[a1] + len[a2])
        index_re = 0
        while i < len(a1):
            while j < len(a2):

                if a1[i] < a2[j]:
                    re[index_re] = a1[i]
                    i = i + 1
                    index_re = index_re + 1
                else:
                    re[index_re] = a2[i]
                    j = j + 1
                    index_re = index_re + 1
                    
                return re
                
def media1(a1, a2):
        re = merge_sort(a1, a2)
        # return based on odd or even

#solution O(log(m+n) )
def media2(a1, a2):
        length = len(a1) + len(a2)
        arr = a1 + a2
        result = None
        #odd
        if length % 2 == 1:
            k = (length + 1) / 2 - 1 
            result = kth_ele(arr, k)
        else:
            k1 = length/2
            k2 = length/2 + 1
            result = (kth_ele(arr, k1) + kth_ele(arr, k2)) / 2.0

        return result
    
def kth_ele(array, k):
        pilot = array[0]
        left = []
        right = []
        for ele in array:
            if ele <= pilot:
                left.append(ele)
            else:
                right.append(ele)

        if len(left) == k:
            return pilot
        elif len(left) > k:
            return kth_ele(left, k)
        else:
            return kth_ele(right, k-len(left))
            
    






# Complete the function below.
# @return the third-latest date (Date object) from dates (list of Date objects)
def third_latest(dates):
    iarray = [x.split('-') for x in dates]
    arr_int = []
    for ele in iarray:
        #s = ele[2]+ele[1]+ele[0]
        #i = int(s)



        arr_int.append(ele)
    re =  kth_element(arr_int, len(arr_int) - 3)

#    s = str(re)
#    re_return = s[6:8]+'-'+s[4,6]+'-'+s[0:4]
    return re


def kth_element(narray, k):
    #newn = [None] + n
    target = narray[0]

    left = []
    right = []
    
    for ele in narray[1:]:
        if (ele < target):
            left.append(ele)            
        elif (ele > target):
            right.append(ele)
        else:
            continue
    
    if (len(left) > k - 1):
        return kth_element(left, k)
    elif (len(left) < k - 1):
        return kth_element(right, k-len(left)-1)
    else:
        return target


if __name__ == "__main__":
#        s = "aaa"
#        if type(s) == <type 'str'>
        a1 = [14-04-2001, 29-12-2061, 21-10-2019, 07-01-1973, 19-07-2014, 11-03-1992, 21-10-2019]
#    for ele in  a1:
#            print ele.year

#    print third_latest(a1)       
