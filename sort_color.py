# 
# Your previous Plain Text content is preserved below:
# 
# //func([5,-4,3,2,1]) = [5,-4,3,2,1]
# //func(3,-4,3,2,1]) = [3,2,1]
# 
# 
# 
# 
# 

# max_subarray(i) = max(sum(j) - sum(k)) where i > j > k
# m[i] = sum(0, i) 
# max_subarray = max(m[end]) - min(m[start])
def max_subarray(array):
        

    if len(array) == 0:
        return 0

    m = {}
    m[0] = array[0]
    
#    d={}
#    d[0] = (array[0], 0, 0)
    i = 1
    while i < len(array):

        m[i] = (m[i-1] + array[i])
        i += 1
        
    maxi = 0
    end = -1
    for i in range(len(array)):
        if m[i] > maxi:
            maxi = m[i]
            end = i

    mini = 0
    start = -1
    for j in range(p):
        if m[j] < mini:
            mini = m[j]
            start = j        
    
    return array[start+1 : p+1]
        



    
#        now = array[i]
#        previous = d[i-1][0] + array[i]
#        previous_raw = d[i-1][0]
        

        

            
#        if now > 0:
#            if previous > now :
                
#                d[i] = (previous, d[i-1][1], i)
#            else:
#                d[i] = (now, i, i)
#        elif previous > previous_raw:
#            d[i] = (now, d[i-1][1], i)
#        else:
#            d[i] = (d[i-1][0], d[i-1][1],d[i-1][2])
#        i +=1
        
#    return array[ d[len(array) - 1][1] : d[len(array) - 1][2] +1 ]
        
        
def max(a, b ):
    if a > b:
        return a
    else:
        return b
    
    
if __name__ == "__main__":
    a = [3,8,5,-20,3,2,1]
    result = max_subarray(a)
    print result
