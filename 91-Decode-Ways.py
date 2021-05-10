class Solution:
    def numDecodings(self, s: str) -> int:
        # 分支决策， dfs
        self.res = 0
        # N = len(s)
        from functools import lru_cache
        @lru_cache(256)
        def dfs(remains):
            res = 0
            if remains == "":
                return 1
            if len(remains)>1 and 10<=int(remains[:2])<=26:
                res += dfs(remains[2:])
            if remains[0] != "0":
                res += dfs(remains[1:])
            return res
        self.res = dfs(s)
        return self.res
