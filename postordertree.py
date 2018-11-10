# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


        

class Solution(object):
    def __init__(self):
        self.re = []
    
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.postorder_put_list(root)
        return self.re
        
        
    def postorder_put_list(self, root):
        if root == None:
            return 
        else:
            self.postorder_put_list(root.left)
            self.postorder_put_list(root.right)
            self.re.append(root.val)
