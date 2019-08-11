from functools import lru_cache
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # basic dp. don't think too much
        @lru_cache(30000)
        def helper(d, f, target):
            if d*f<target or target<d:
                return 0
            if d == 1:
                return 1
            else:
                res = 0
                for i in range(1,f+1):
                    res += helper(d-1,f,target-i)
                return res
        return helper(d, f, target)%(10**9+7)
