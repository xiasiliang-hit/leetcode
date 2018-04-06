# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.in_order = []
            
        return 
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.inorder_tree(root)
        return self.in_order
        
    def inorder_tree(self, root):
        if root == None:
            return 
        
        self.inorder_tree(root.left)
        self.in_order.append(root.val)
        self.inorder_tree(root.right)
        
        
