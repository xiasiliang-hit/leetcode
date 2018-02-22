def scan(array):
    appear = {}
    for astr in array:
        for ch in astr:
            if ch in appear.keys():
                appear[ch].append(astr)
            else:
                appear[ch] = [astr]
    return appear

def find_frequent(ch, di):
    exist = {}
    list_str = di[ch]
    for astr in list_str:
        for ele in astr:
            if ele != ch:
                if ele in exist.keys():
                    exist[ele] = exist[ele] + 1
                else:
                    exist[ele] = 1

    max = 0
    re = ""
    for i in exist.keys():
        if exist[i] > max:
            max = exist[i]
            re = i
        elif exist[i] == max:
            re = re + i
        else:
            continue

    return re.replace(ch, '')

def begin(array):
    di = scan(array)
#    print di
    for i in di.keys():
        re = find_frequent(i, di)

        print i, ":", re


if __name__ == "__main__":
    array  = ["abc", "bcd", "def"]
    begin(array)        
