class Solution:
    def deleteString(self, s: str) -> int:
        # dp problem dp[i] = max(1, dp[j]+1) if s[i:j]==s[j:j+j-i]
        L = len(s)
        dp = [1]*L
        dp[-1] = 1
        for i in range(L-1,-1,-1):
            for j in range(i+1,(L+i)//2+1):
                if dp[j]+1>dp[i]:# this can significantly reduce the runtime
                    if s[i:j] == s[j:2*j-i]:
                        dp[i] = dp[j]+1#max(dp[i], dp[j]+1)
        # print(dp)
        return dp[0]
