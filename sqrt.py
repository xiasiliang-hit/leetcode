# AC

def sqrt(x):
    left = 1
    right = x

    mid = (left + right) / 2

    while True:
        print mid
        if mid * mid > x:
            right = mid
            mid = (left + right) / 2
        elif mid*mid <= x and (mid+1) * (mid+1) > x:
            return mid
        else:
            left = mid
            mid = (left + right) / 2



if __name__ == "__main__":
    print sqrt(36)
    
