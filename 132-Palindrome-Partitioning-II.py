class Solution:
    def minCut(self, s: str) -> int:
        # res = []
        self.res = float('inf')
        from functools import lru_cache
        @lru_cache(2048)
        def isPalindrome(s):
            return s == s[::-1]
        dp = [float('inf')]*(len(s)+1)
        dp[0] = -1
        for i in range(1,len(s)+1):
            for j in range(i):
                if isPalindrome(s[j:i]):
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]
