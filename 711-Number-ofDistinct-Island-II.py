class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
        # write your code here
        if not grid or len(grid[0]) == 0:
            return 0
        lrc, visited, ans, shapes = [len(grid), len(grid[0])], set(), [0], set()
        def dfs(i,j):
            if 0<=i<lrc[0] and 0<=j<lrc[1] and grid[i][j] and (i,j) not in visited:
                visited.add((i,j))
                shape.append((i,j))
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        def addShape(shape, shapes):
            xs,ys = zip(*shape)
            xMin,yMin = min(xs), min(ys)
            island0 = tuple(sorted((x-xMin,y-yMin) for x, y in shape))
            if island0 in shapes:
                return
            ans[0] += 1
            xs, ys = zip(*island0)
            xMax, yMax = max(xs), max(ys)
            island1 = tuple(sorted((-x+xMax, y) for x,y in island0))
            island2 = tuple(sorted((x,-y+yMax) for x, y in island0))
            island3 = tuple(sorted((-x+xMax,-y+yMax) for x,y in island0))
            island4 = tuple(sorted((y,x) for x,y in island0))
            island5 = tuple(sorted((-y+yMax,x) for x,y in island0))
            island6 = tuple(sorted((-y+yMax,-x+xMax) for x,y in island0))
            island7 = tuple(sorted((y,-x+xMax) for x,y in island0))
            
            shapes.update([island0,island1,island2,island3,island4,island5,island6,island7])
            # or use
            # shapes|=([island0,island1,island2,island3,island4,island5,island6,island7])
        for i in range(lrc[0]):
            for j in range(lrc[1]):
                shape = []
                dfs(i,j)
                if shape:
                    addShape(shape,shapes)
        print(shapes)
        return ans[0]
