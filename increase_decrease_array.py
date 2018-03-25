import pdb

def increase_decrease(array, head, end):
    if end == head:
        return array[head]
    
    i = (head+end) / 2    
    if i-1>=0 and i+1 <= len(array)-1:
        if array[i-1] <=array[i]  and array[i] <= array[i+1]:
            return increase_decrease(array, i+1, end)
        elif array[i-1] <= array[i] and array[i] >= array[i+1]:
            return array[i]
        else: #array[i-1] >= array[i] and array[i] >= array[i+1]:
            return increase_decrease(array, head, i)

    else:
        return array[i]


if __name__ == "__main__":
    array = [5,4,3]
    print increase_decrease(array, 0, len(array)-1)
            
