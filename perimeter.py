import pdb


class Solution:
    def __init__(self):
        return

    def cal(self, grid, X, Y):
        peri = 0

        
        for i in range(0, X):
            for j in range(0, Y):
                if grid[i][j] == 1:
                    peri = peri + 4 - self.check_neighbour(grid, X, Y, i, j)

        return peri
        
    def check_neighbour(self, grid, X, Y, i, j):
        count = 0
        neighbours= []
        indexs =  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for ind in indexs:
            if (ind[0] >= 0 and ind[0] <= X - 1 and ind[1] >= 0 and ind[1] <= Y - 1):
                neighbours.append(grid[ind[0]][ind[1]])
        
        for ele in neighbours:
            if ele == 1:
                count = count + 1
            
        return count


    
if __name__ == '__main__':
    s = Solution()
    print s.cal([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 4, 4)
