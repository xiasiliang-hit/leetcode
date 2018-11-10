# test case is wrong I think

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root == None:
            return False
        
        q = [(root, sum-root.val)] 
        print sum-root.val
        while q != []:
            ele = q.pop()
            node = ele[0]
            target = ele[1]
            
            if ele[1] == 0:
                return True
            
            elif ele[1] < 0:
                pass
            
            else:
                if node.left != None:

                    q.append( (node.left, target - node.left.val) )
                if node.right != None:
                    q.append( (node.right, target - node.right.val) )
        
        return False
        
        
