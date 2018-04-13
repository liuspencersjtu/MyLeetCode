class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        original_height_sum = sum([sum(i) for i in grid])
        left_right = [max(i) for i in grid]
        
        gridTranverse = [[] for i in grid]
        for i in range(len(gridTranverse)):
            gridTranverse[i] = [grid[j][i] for j in range(len(grid))]
        bottom_top = [max(i) for i in gridTranverse]
        
        gridNew=[[0 for j in i] for i in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                gridNew[i][j] = min(left_right[j],bottom_top[i])
                
        final_height_sum = sum([sum(i) for i in gridNew])
        
        return final_height_sum - original_height_sum