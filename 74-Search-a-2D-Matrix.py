class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        i = 0
        n=len(matrix)
        while i<n and matrix[i][0]<target:
            i+=1
        print(i)
        if i>0:
            for item in matrix[i-1]:
                if item == target:
                    return True
        if i<n:
            for item in matrix[i]:
                if item == target:
                    return True
        for item in matrix[0]:
            if item == target:
                return True
        return False    