from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        @lru_cache(10000)
        def helper(i, M):
            curSum = 0
            # curM = 0
            if N-i<=2*M:
                return sum(piles[i:])
            for x in range(1,2*M+1):
                tmp = sum(piles[i:]) - helper(i+x, max(M,x))
                if tmp>curSum:
                    curSum = tmp
                    # curM = x
            return curSum   
        return helper(0,1)
