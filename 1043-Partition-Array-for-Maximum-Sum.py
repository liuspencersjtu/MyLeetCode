from functools import lru_cache
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        @lru_cache()
        def dp(i):
            cur = 0
            if i<K:
                return max(A[:i+1])*(i+1)
            else:
                for j in range(1,K+1):
                    cur = max(cur, dp(i-j)+max(A[i-j+1:i+1])*j)
                return cur
        return dp(len(A)-1)
            
