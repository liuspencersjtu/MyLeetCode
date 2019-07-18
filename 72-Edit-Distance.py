class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(word1, word2, m, n):
            if (m,n) in memo:
                return memo[(m,n)]
            if m==0:
                memo[(m,n)]=n
                return n
            if n==0:
                memo[(m,n)]=m
                return m
            if word1[m-1]==word2[n-1]:
                res =  dp(word1, word2, m-1, n-1)
                memo[(m,n)]=res
                return res
            else:
                res = min(dp(word1, word2, m-1, n), dp(word1, word2, m, n-1), dp(word1,word2, m-1,n-1))+1
                memo[(m,n)]=res
                return res
        return dp(word1, word2, len(word1), len(word2))
