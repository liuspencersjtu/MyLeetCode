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
