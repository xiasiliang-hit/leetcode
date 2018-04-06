def jump(nums):
    flag = False
    que = [(0, nums[0])]
    
    if (len(nums) == 1):
        return True

    while len(que) != 0:
        ind,step = que.pop()

        for i in range(1, step+1):

                
            if (ind+i) == len(nums) - 1:
                flag = True
            elif (ind+i < len(nums) - 1):
                que.append((ind+i, nums[ind+i]))
    return flag


                           
if __name__ == "__main__":
    array = [4,3,2,1,0,4]
    print jump(array)
    
