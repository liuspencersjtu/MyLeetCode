class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        if not matrix[0]:
            return 0
        n = len(matrix[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        i ,j = 1, 1
        maxside = 0
        while i<=m:
            while j<=n:
                #print(matrix[i-1][j-1])
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    #print(i,j,dp[i][j])
                    if dp[i][j]>maxside:
                        maxside = dp[i][j]
                j+=1
            j =1
            i+=1
        return maxside*maxside