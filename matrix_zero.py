# 73. Set Matrix Zeroes

# should record coordinate then operate


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        coordw = []
        coordh = []
        
        h = len(matrix)
        w = len(matrix[0])
        
        for i in range(0, w):
            for j in range(0, h):
                if matrix[j][i] == 0:
                    coordw.append(i)
                    coordh.append(j)
                    
        for i in coordw:
            for j in range(0, h):
                matrix[j][i] = 0
                        
        for j in coordh:
            for i in range(0, w):
                matrix[j][i] = 0



if __name__ == '__main__':

    matrix = [[1 for i in range(0, 10)] for j in range(0, 10)]

#    for i in range(0, 10):
#        matrix[i] = [[1]*10]

    matrix[0][0] = 0
    matrix[2][2] = 0

    print matrix
    
    solution = Solution()
    s = solution.setZeroes(matrix)
    print matrix
    
