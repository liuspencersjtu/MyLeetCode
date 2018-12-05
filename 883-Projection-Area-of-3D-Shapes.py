class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for item in grid:
            for i in item:
                if i:
                    res+=1
        res+=sum([max(i) for i in grid])+sum([max(i) for i in zip(*grid)])
        return res
