class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # dijkstra
        import heapq
        m, n = len(grid), len(grid[0])
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        hashmap = [[0,0,0]] # t, row, column
        visited = set()
        while hashmap:
            t, r, c  = heapq.heappop(hashmap)
            if (r,c) in visited:
                continue
            if r==m-1 and c==n-1:
                return t
            visited.add((r,c))
            for i,j in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
                if 0<=i<m and 0<=j<n:
                    if grid[i][j]<=t+1:
                        heapq.heappush(hashmap, [t+1, i, j])
                    else:
                        gap = grid[i][j]-t
                        heapq.heappush(hashmap, [grid[i][j]+(1+gap)%2, i, j])

