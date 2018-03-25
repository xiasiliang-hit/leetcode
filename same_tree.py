# works !

import pdb


def same_tree(p, q):
    if p == None and q == None:
        return True
    if (p == None and q != None) or (p != None and q == None):
        return False
    if p.val == q.val:
        if same_tree(p.left, q.left) == True and same_tree(p.right, q.right) == True:
            return True
        else:
            return False
    else:
        return False

