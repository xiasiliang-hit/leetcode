# not work
import sys

MAX_INT = sys.maxint
class Solution(object):
    def minPathSum(self, grid):
        d = {}
        X = len(grid[0])
        Y = len(grid)
        i = 0
        j = 0
        d[(0,0)] = grid[0][0]
        d[(0,1)] = grid[0][0] + grid[0][1]
        d[(1,0)] = grid[0][0] + grid[1][0]
    
        print d[(0,0)]
        while j < Y:
            i = 0
            while i < X:
                if i == 0 and j == 0:
                    continue 
                    
                if i >= 1:
                    a = d[( j, i-1)] + grid[j][i]
                else:
                    a = MAX_INT
                if j > 1:
                    b = d[(j-1, i)] + grid[j][i]
                else:
                    b = MAX_INT

                print self.min(a,b)
                d[(j, i)] = self.min(a,b)
                i+=1
            j+=1
        print d
        return d[(Y-1, X-1)]
        
         
    def min(self, x, y):
        if x < y:
            return x
        else:
            return y
