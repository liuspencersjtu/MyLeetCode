class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j]==2:
                    queue.append((i,j))
        cnt = 0
        while queue:
            cnt += 1
            newqueue = []
            for a,b in queue:
                grid[a][b]=0
                for a1,b1 in {(a-1,b),(a+1,b),(a,b+1),(a,b-1)}:
                    if 0<=a1<m and 0<=b1<n and (a1,b1) not in queue and grid[a1][b1]==1:
                        newqueue.append((a1,b1))
            queue = newqueue
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j]==1:
                    return -1
        return max(cnt-1,0)
