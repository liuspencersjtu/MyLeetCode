class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 二维dp问题, 2D dp question
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        def findLongestFromHere(i,j,mat,dp):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            candidate = []
            if (j<n-1 and mat[i][j]<mat[i][j+1]):
                candidate.append(1+findLongestFromHere(i,j+1,mat,dp))
            if (j>0 and mat[i][j]<mat[i][j-1]):
                candidate.append(1+findLongestFromHere(i,j-1,mat,dp))
            if (i<m-1 and mat[i][j]<mat[i+1][j]):
                candidate.append(1+findLongestFromHere(i+1,j,mat,dp))
            if (i>0 and mat[i][j]<mat[i-1][j]):
                candidate.append(1+findLongestFromHere(i-1,j,mat,dp))
            candidate.append(1)
            dp[i][j] = max(candidate)
            return dp[i][j]
        
        dp = [[-1 for j in range(n)] for i in range(m)]
        
        res = 1
        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    res = max(res, findLongestFromHere(i,j,matrix,dp))
        return res

