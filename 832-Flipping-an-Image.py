class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l = len(A)
        B=[[]]*l
        for i in range(l):
            B[i] = [0]*l
            
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[i][l-1-j] = 1 if A[i][j] == 0 else 0
                    
        return B