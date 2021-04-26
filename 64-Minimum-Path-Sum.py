class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 1:
            return sum(grid[0])
        if len(grid[0]) == 1:
            return sum([item[0] for item in grid])
        a = grid[0][0] + self.minPathSum(grid[1:])
        b = grid[0][0] + self.minPathSum(zip(*[zip(*grid)][1:]))
        return min(a,b)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if i == 0:
                    if j != 0:
                        grid[i][j] += grid[i][j-1]
                elif j == 0:
                    if i != 0:
                        grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[M-1][N-1]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 递归太慢了
        M, N = len(grid), len(grid[0])
        @lru_cache(10000)
        def helper(m,n):
            if m==0:
                return sum(grid[0][:n+1])
            elif n==0:
                return sum(list(zip(*grid))[0][:m+1])
            else:
                return grid[m][n]+min(helper(m-1,n),helper(m,n-1))
        return helper(M-1,N-1)
                
            
