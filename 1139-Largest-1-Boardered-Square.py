class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        res = 0
        def check(p1,p2):
            for i in range(p1[0],p2[0]+1):
                if grid[i][p1[1]]==0:
                    return False
                if grid[i][p2[1]]==0:
                    return False
            for j in range(p1[1],p2[1]+1):
                if grid[p1[0]][j]==0:
                    return False
                if grid[p2[0]][j]==0:
                    return False
            return (p2[0]-p1[0]+1)**2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    # get first pointer at (i,j)
                    for k in range(min(m-i,n-j)):
                        res = max(res, check((i,j),(i+k,j+k)))
        return res
    
