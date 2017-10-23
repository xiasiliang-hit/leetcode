import pdb
from random import shuffle

class TreeNode(object):
     def __init__(self, data):
         self.val = data
         self.left = None
         self.right = None

         self.begin = self
         self.end = self
                
     def binary_search(self, root, val):
         current = root
         path = []
                  
         while (current != None ):
             path.append(current)
             if (current.val == val):
                 return current
             elif (current.val > val):
                 current = current.left
             else:
                 current = current.right
         return path
     
global res
class BST(object):

    #build BST tree from array 
    def __init__(self, array):
        self.root = None
        self.root = BST.build_tree(array)
        self.size = len(array)
        global res
        res = []

    @staticmethod
    def insert(node, someNumber):
        if node is None:
            return TreeNode(someNumber)
        else:
            if  someNumber > node.val:
                if node.right is not None:
                    BST.insert(node.right, someNumber)
                else:
                    node.right = TreeNode(someNumber)
                    return node.right
            else:
                if node.left is not None:
                    BST.insert(node.left, someNumber)
                else:
                    node.left = TreeNode(someNumber)
                    return node.left
                
    @staticmethod
    def build_tree(array):
        root = TreeNode(array[0])

        for e in array[1:]:
            BST.insert(root, e)

        return root
    
    def print_tree(self):
        in_order(self.root)
        print res




def in_order(root):
    current = root
    if (current != None):
            in_order(current.left)
            #print current.val
            res.append(current.val)
            in_order(current.right)
            

#
#def convert_to_CDLlist2(root):

#    if root.left is None and root.right is None:
#        root.left = root
#        root.right = root
#        return root

#    else:
#        tail = convert_to_CDLlist2(root.left)
#        tail.right = root
#        root.left = tail
        
#        head2 = convert_to_CDLlist2(root.right)
#        head2.left = root
#        root.right = head2
        
#        return root


#two steps:
# 1 modify the tree to double linked list
# 2 connect the head and tail

def convert_to_CDLlist(tree):
    head, tail = convert(tree.root)

    head.left = tail
    tail.right = head
    
    return (head, tail)


# convert to a double linked list
# each iteration expand a lower layer beginning from root, greedly
# maintain the recursion assumption that root.begin and root.end always specified the head and end of#  the linked list  
def convert(root):
        
#    if (root.val == 4):
#        pdb.set_trace()

    if (root.left is None and root.right is None):
#        root.left = root
#        root.right = root
        return (root, root)

    else:
        if root.left is not None:
            (head,tail) = convert(root.left)

            root.begin = head  # keep the head pointer of linkedlist        
            tail.right = root
            root.left = tail
            #        return (head, root.end)

        if root.right is not None:
            (head, tail) = convert(root.right)
            
            root.end = tail # keep the end pointer of linkedlist
            head.left = root
            root.right = head
        
        return (root.begin, root.end)   
    

# connect head and tail so that it is circular 
# def connect(root):
#     #find head
#     current = root
#     while (current.left is not None):
#         current = current.left
#     head = current

#     #find tail
#     current2 = root
#     while (current2.right is not None):
#         current2 = current2.right

#     tail = current2
    
#     head.left = tail
#     tail.right = head
    
#     return (head, tail)


#SMALL: data of left end of list used as termination 
#BIG: data of right end of list used as termination
def test(head,tail, SMALL, BIG):    
    
    #test1 from head to right
    print "#test1 from head to tail (by right link"
    c = head
    while(True):
        print c.val
        c = c.right    
        if c.val == SMALL:
            break
        
    #test 2 from head to left 
    print  "#test 2 from head to tail (left link)"
    c = head 
    while (True):
        print c.val
        c = c.left
        if c.val == SMALL:
            break


    #test 3 from tail to left
    print  "#test 3 from tail to left"
    c = tail
    while (True):
        print c.val
        c = c.left

        if c.val == BIG:
            break
        

    #test 4 from tail to right
    print "#test 4 from tail to right"
    c = tail
    while (True):
        print c.val
        c = c.right

        if c.val == BIG:
            break 
    
#test from tail to right, do not break, runs forever casue it is a circle
#    c = head
#    while (True):
#        print c.val
#        c = r.right

    return


if __name__ == '__main__':

    #test manual input
    tree = BST([0,1,3,2,5,4])
    tree.print_tree()
    head, tail = convert_to_CDLlist(tree)
    test(head, tail, 0, 5)


    #test random input
    N = 20
    a = range(N)
    shuffle(a)
    tree = BST(a)
    head, tail = convert_to_CDLlist(tree)        
    test(head,tail, 0, N-1)

    # does not work
    #    head, tail = convert_to_CDLlist2(tree.root)
    #    test(head,tail, 1,6)
