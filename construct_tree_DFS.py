import pdb

def construct_tree(line):
    if check() == False:
        
        return
    else:
        pairs = line.split(' ')
        d = {}

        parents = []
        children = []
        
        #construct dict
        for p in pairs:
            parent = p[1]
            child = p[3]

            parents.append(parent)
            children.append(child)

            if parent in d.keys():
                d[parent].append(child)
            else:
                d[parent] = [child]

        root = None
        for r in parents:
            if r not in children:
                root = r

        current  = root
        stack = []

        print "(",
        stack.append(")")
        
        stack.append(current)
        while len(stack) != 0:
            parent = stack.pop()
            print  parent,
            if parent == ')':
                continue
            
            if parent in d.keys():
                print "(",
                stack.append(")")            
                if len(d[parent]) == 2:
                    stack.append(d[parent][0])
                    stack.append(d[parent][1])
                else:
                    stack.append(d[parent][0])
    return

def check():
    return True


if __name__ == "__main__":
    s = "(A,B) (A,C) (C,E), (C,F),(B,R)"
    construct_tree(s)
    
