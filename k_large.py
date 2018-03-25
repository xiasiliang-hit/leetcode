import pdb

def k_large(array, k):
    left = []
    right = []

    pilot = array[0]
    for i in range(len(array)):
        if array[i] <= pilot:
            left.append(array[i])
        else:
            right.append(array[i])

    if len(left) == k:
        return pilot
    elif len(left) > k:
        return k_large(left, k)
    else:
        return k_large(right, k - len(left))

if __name__ == "__main__":
    array = [1,2,6,3,4,5]
    print k_large(array, 3)
