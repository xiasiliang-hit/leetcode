# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        q = [root]
        q1 =[root]
        
        relist = [root.val]
        re = []
        
        while q1 != []:
            print q 
            q = list(q1)
            q1 = []
            relist=[]
            
            for ele in q :
                
                relist.append(ele.val)
                
                #re.append(ele)

                if ele.left !=  None: 
                    q1.append(ele.left)
                    
                    
                if ele.right != None:
                    q1.append(ele.right)
                    
                    
            re.append(relist)
            
            
            
        return re
        
