# works

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        
        X= len(matrix[0])
        Y = len(matrix)
        
        i = 0
        j = (Y-1)
        while i<X and j>= 0: 
            print matrix[j][i]
            if target == matrix[j][i]:
                return True
            elif target > matrix[j][i] :
                i += 1
            else:
                j -= 1
        return False
        
            
            
        
