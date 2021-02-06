class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     # 超时算法，中间travel的时候重复访问太多了
    #     self.res = 0
    #     def travel(x,y):
    #         # 如果终点没有障碍，到尽头就+1
    #         if x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1 and obstacleGrid[x][y] != 1:
    #             self.res += 1
    #         if x + 1 <= len(obstacleGrid) - 1 and obstacleGrid[x+1][y] != 1:
    #             travel(x+1, y)
    #         if y + 1 <= len(obstacleGrid[0]) - 1 and obstacleGrid[x][y+1] != 1:
    #             travel(x, y+1)
    #     # 如果初始位置有障碍，那么一定没有路了
    #     if obstacleGrid[0][0] == 1:
    #         return 0
    #     travel(0, 0)
    #     return self.res
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 在上一个基础上改进，带memo的递归
        cache = {}
        def travel(x,y):
            if (x,y) in cache:
                return cache[x,y]
            res = 0
            if obstacleGrid[x][y] == 0:
                if x + 1 <= len(obstacleGrid) - 1:
                    res += travel(x+1, y)
                if y + 1 <= len(obstacleGrid[0]) - 1:
                    res += travel(x, y+1)
                if x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1:
                    res += 1
            cache[x, y] = res
            return cache[x, y]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            return travel(0, 0)
        
        
