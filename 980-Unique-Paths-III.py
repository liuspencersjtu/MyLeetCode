class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        
        def neighbours(r,c):
            for r1,c1 in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
                if 0<=r1<R and 0<=c1<C and grid[r1][c1]!=-1:
                    yield [r1,c1]
        
        todo = 1
        #finding start and end points and counts the steps
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if grid[r][c]==0:
                    todo+=1
                if grid[r][c]==1:
                    rs,cs=r,c
                if grid[r][c]==2:
                    rt,ct=r,c
        
        #backtracing
        self.res = 0
        def dfs(r,c,todo):
            if todo<0:
                return
            if todo==0:
                if r==rt and c==ct:
                    self.res+=1
            todo-=1
            grid[r][c]=-1
            for r1,c1 in neighbours(r,c):
                dfs(r1,c1,todo)
            grid[r][c]=0
            return
        
        dfs(rs,cs,todo)
        return self.res
