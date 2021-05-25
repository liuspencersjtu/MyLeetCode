class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from functools import lru_cache
        @lru_cache(128)
        def fractional(n):
            if n==0:
                return 1
            res = 1
            for i in range(1,n+1):
                res *= i
            return int(res)
        def combination(n,k):
            return int(fractional(n)//fractional(n-k)//fractional(k))
        res = []
        for i in range(rowIndex+1):
            res.append(combination(rowIndex,i))
        return res
