class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # this pythonic solution won't work
        # matrix[:] = zip(*matrix[::-1])
        #先上下翻转，再左上右下对角线翻转
        n = len(matrix)
        # upside down
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        # reflect by top-left to bottom-right
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
