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