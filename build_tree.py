def build():
    line = raw_input()
    pairs = line.split(' ')
    
    if check(pairs) != True:
        return check(pairs)
    else:
        build_tree()    


def check(array):

#    print array
#    abc = range('a','a' + 26)
    for e in array:
        if len(e) != 5:
            return 'E1'
        
        elif e[0] != '(' or e[4] != ')':
            return 'E1'

        else:
            continue
    #
    i = 0
    j = 0
    while i <  len(array):
        j = i + 1
        while j < len(array):
            if array[i] == array[j]:
                return 'E2'
            j = j+1
        i=i+1
        
    #
    d = {}
    dchild = {}
    for e in array:
        parent = e[1]
        child = e[3]

        if parent in d.keys():
            if d[parent] == 2:
                return 'E3'
            else:
                d[parent] = d[parent]+1
        else:
            d[parent] = 1

        if child in dchild.keys():
            if dchild[child] == 2:
                return 'E4'
            else:
                d[child] = d[child]+1
        else:
            d[child] = 1

    return False

def build_tree(tree_dict):

    root=
    
    return 


if __name__ == "__main__":

    d = {"a": 123}
    for e in d:
        print e


    
    
    
#    s = '(a,b) (a,c) (a,e)'
#    a = s.split(' ')
#    print a
#    print check(a)


