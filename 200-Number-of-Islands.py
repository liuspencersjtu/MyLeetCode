class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def surround(i,j):
            res = []
            m = len(grid)
            n = len(grid[0])
            if i>0:
                res.append([i-1,j])
            if i<m-1:
                res.append([i+1,j])
            if j>0:
                res.append([i,j-1])
            if j<n-1:
                res.append([i,j+1])
            return res
                
        def shrink(i,j):
            if grid[i][j]=='1':
                grid[i][j]='0'
                for m,n in surround(i,j):
                    shrink(m,n)            
        res = 0
        for i, line in enumerate(grid):
            for j, val in enumerate(line):
                if grid[i][j]=='1':
                    res+=1
                    shrink(i,j)
        return res

 class Solution:
    def NumberofIsland(self, imag):
        if len(imag) or len(imag[0]): # empty matrix
            return 0
        
        row = len(imag)
        col = len(imag[0])
        
        count = 0
        for i in range(row):
            for j in range(col):
                if imag[i][j] == '1':
                    count += 1
                    self.helper(imag, row, col, i, j)
        return count
        
    def helper(self, imag, row, col, i, j):
        # check boundary
        if i<0 or i>row-1 or j<0 or j>col-1 or imag[i][j]!='1':
            return
        imag[i][j] = 'x'   # label 1
        self.helper(imag, row, col, i+1, j)  # upper
        self.helper(imag, row, col, i-1, j)  # lower
        self.helper(imag, row, col, i, j+1)  # right
        self.helper(imag, row, col, i, j-1)  # left
