import pdb
import Queue


class Solution(object):
    #visited = []
    #nComponent = True
    #matrix = None

    def __init__ (self, matrix):
        self.matrix = matrix
        self.visited = [False]*len(matrix)
        self.nComponent = 0

        
    def solution (self):
        i = 0
        while i < len(self.matrix) and self.visited[i] == False:
#            self.visited[i] = True
            self.expend(i)
            i = i + 1

#        print self.nComponent
        return self.nComponent
        
    def expend(self, node):
        q = Queue.Queue()
        q.put(node)
        
        while q.empty() != True:
            i = q.get()
            self.visited[i] = True
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1 and self.visited[j] == False:

                    q.put(j)
#                    self.visited[j] == True

        self.nComponent = self.nComponent + 1
        return 
    
                
if __name__ == "__main__":
    
    m = [[1,1,0,0], [1,1,0,0], [0,0,1,1], [0,0,1,1]]
    s = Solution(m)
    print   s.solution()


