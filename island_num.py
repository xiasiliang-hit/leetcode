## now work !

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
        
        visited = [[False for x in range(X) ] for y in range(Y)]
        self.num = 0
        
    def island_num(self):
        #X = len(matrix[0])
        #Y = len(matrix)
        for j in range(Y):
            for i in range(X):                
                if visited[j][i] == False and matrix[j][i] == 1:
                    self.expand(i, j)


#                elif matrix[j][i] == 0:
#                    visited[j][i] = True
#                    continue

                print visited
                
        return self.num
                    
    def expand(self, coordx, coordy):
#        X = len(matrix[0])
#        Y = len(matrix)
        print coordx, coordy

        q = Queue.Queue()
        q.put((coordx, coordy))
#        visited[coordy][coordx] = True
        
        while q.empty() is False:
            (i, j) = q.get()
            visited[j][i] = True
            around = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            tested = filter(lambda coord : coord[0]>=0 and coord[0]<= X-1 and coord[1] >= 0 and coord[1] <= Y-1, around)
            
            for coordxy in tested:
                print coordxy
                if visited[coordxy[1]][coordxy[0]] == False and  matrix[coordxy[1]][coordxy[0]] == 1:
                    q.put(coordxy)

        
        self.num = self.num + 1



if __name__ == "__main__":

    global matrix
    matrix = [[0,1],[1,0], [0,1],[1,0]]
    
    
    s = Solution()
    print s.island_num()
    
