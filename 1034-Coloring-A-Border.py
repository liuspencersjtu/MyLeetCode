class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        seen, m, n = set(), len(grid), len(grid[0])
        
        def dfs(x,y):
            if (x,y) in seen: return True
            if not (0 <=x < m and 0 <=y < n and grid[x][y] == grid[r0][c0]):
                return False
            seen.add((x,y))
            if dfs(x+1,y)+dfs(x-1,y)+dfs(x,y+1)+dfs(x,y-1) < 4:
                grid[x][y] = color
            return True
        dfs(r0, c0)
        return grid



###### BFS Solution
import copy
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        M,N = len(grid), len(grid[0])
        visited = set([(r0,c0)])
        border = set()
        bfs = [[r0,c0]]
        while bfs:
            r,c = bfs.pop(0)
            visited.add((r,c))
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<=r+a<M and 0<=c+b<N and grid[r+a][c+b] == grid[r0][c0]:
                    if (r+a,c+b) not in visited:
                        bfs.append([r+a,c+b])
                else:
                    border.add((r,c))
        for r,c in border:
            grid[r][c]=color
        return grid
