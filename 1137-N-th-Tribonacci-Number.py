from functools import lru_cache
class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(10000)
        def helper(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            return helper(n-1)+helper(n-2)+helper(n-3)
        return helper(n)
