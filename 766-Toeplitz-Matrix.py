class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return True
        for i in range(m-1):
            if matrix[i][:n-1] != matrix[i+1][1:]:
                return False
        return True
            