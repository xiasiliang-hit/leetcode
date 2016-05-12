import pdb




def add_digits(num):

    if len(str(Num)) == 1:
           return num

    else:           
        pdb.set_trace()
        n = 0
        for s in str(num):
           n = n + int(s)

        return add_digits(n)





if __name__ == '__main__':
    print add_digits(10)
