from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        @lru_cache(10000)
        def helper(target):
            if target<0:
                return 0
            if target == 0:
                return 1
            res = 0
            for it in nums:
                res += helper(target-it)
            return res
        if target == 0:
            return 0
        return helper(target)
                
