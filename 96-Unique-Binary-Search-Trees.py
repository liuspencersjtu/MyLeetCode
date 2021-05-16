class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        # bst should be sorted
        from functools import lru_cache
        @lru_cache(256)
        def helper(num):
            if not num:
                return 1
            res = 0
            for i in range(num):
                l = helper(i)
                r = helper(num-i-1)
                res += l*r
            return res
        
        return helper(n)
