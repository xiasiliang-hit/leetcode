## not working

import pdb
import Queue


#visited = []
#matrix = []
#X = 0
#Y = 0
#num = 0

class Solution(object):
    def __init__(self):
        global X, Y, visited, num
        X = len(matrix[0])
        Y = len(matrix)
        
        visited = [[False]*X]*Y
        self.num = 0
        
    def island_num(self):
        #X = len(matrix[0])
        #Y = len(matrix)
        for j in range(Y):
            for i in range(X):                
                if visited[j][i] == False and matrix[j][i] == 1:
                    self.expand(i, j)
                    print visited

                #mark visited
                elif matrix[j][i] == 0:
                    visited[j][i] = True
                    continue
        
        return self.num
                    
    def expand(self, coordx, coordy):
#        X = len(matrix[0])
#        Y = len(matrix)
        print coordx, coordy

        q = Queue.Queue()
        q.put((coordx, coordy))
        visited[coordy][coordx] = True
        
        while q.empty() > 0:
            (j, i) = q.get()

            around = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            tested = [coord for coord in around and coord[0]>=0 and coord[0]<= X-1 and coord[1] >= 0 and coord[1] <= Y-1 ]
            for ele in tested:
                if matrix[ele[0]][ele[1]] == 1:
                    q.put(ele)
                    visited[ele[0]][ele[1]] = True
        
        self.num = self.num + 1



if __name__ == "__main__":

    global matrix
    matrix = [[0,1],[1,0], [0,1]]

    
    s = Solution()
    print s.island_num()
