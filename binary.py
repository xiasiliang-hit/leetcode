import pdb

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """        
        ppath = self.binary_search(self, root, p)
        qpath = self.binary_search(self, root, q)

        m = max(len(ppath), len(qpath))
        
        for i in range(0, m):
            if (ppath[i] != qpath[i]):
                return previous 
            else:
                previous = ppath[i]

                
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

     
     
class Tree(object):
    root, size = None, 0
    def __init__(self, array):
        self.build_tree(array)
        self.root = None
        self.size = len(array)
        self.res = []
        
    def insert(self, node, someNumber):
        if node is None:
            node = TreeNode(someNumber)
        else:
            if node.data > someNumber:
                self.insert(node.rchild, someNumber)
            else:
                self.insert(node.lchild, someNumber)

    def build_tree(self, array):
        for e in array:
            self.insert(None, e)

    def pre_order(self):
        current = self.root
        #res = []
        if (current != None):
            res.append(current.val)
            pre_order(current.left)
            pre_order(current.right)

    def mid_order(self):
        current  = self.root
        if (current != None):
            mid_order(current.left)
            res.append(current.val)
            mid_order(current.right)

    def print_tree(self):
        print self.mid_order()
        
            
if __name__ == '__main__':
    root = TreeNode(4)
#    root.val = 4

    node2 = TreeNode(2)
#    node2.val = 2

    node5 = TreeNode(5)
#    node5.val = 5

    node1 = TreeNode(1)
#    node1.val = 1
    
    node3 = TreeNode(3)
#    node3.val = 3

    root.left = node2
    root.right = node5

    node2.left = node1
    node2.right = node3

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    tree = Tree(arr)
    pdb.set_trace()
    tree.print_tree()
     
    #    print TreeNode.binary_search(root, 4)
