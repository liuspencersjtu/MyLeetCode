class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    # tmp = grid[i][j]
                    # grid[i][j] = 0
                    cur = self.dfs(grid, i, j)
                    res = max(cur, res)
                    # grid[i][j]=tmp
        return res
    
    def dfs(self, grid, i, j):
        tmp = grid[i][j]
        grid[i][j] = 0
        res = 0
        for m,n in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
            if self.is_valid(grid,m,n):
                cur = self.dfs(grid, m, n)
                res = max(cur, res)
        grid[i][j] = tmp
        return res+tmp
    
    def is_valid(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
            return False
        return True
