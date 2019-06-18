class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        N = len(grid)
        queue = [(0,0)]
        level = 1
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        if grid[0][0] == 1:
            return -1
        while queue and level< N*N:
            #print(queue)
            newqueue = set()
            for pos in queue:
                if pos == (N-1, N-1):
                    return level
                visited.add(pos)
                for i, j in directions:
                    if 0<=pos[0]+i<N and 0<=pos[1]+j<N and (pos[0]+i,pos[1]+j) not in visited and grid[pos[0]+i][pos[1]+j]==0:
                        newqueue.add((pos[0]+i, pos[1]+j))
            queue = list(newqueue)
            level += 1
        return -1
