from functools import lru_cache
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        prefix = [0]*(N+1)
        inf = float('inf')
        for i in range(1,N+1):
            prefix[i] = prefix[i-1]+stones[i-1]
        @lru_cache(None)
        def dp(i,j,m):
            if (j-i-(m-1))%(K-1)!=0:
                return inf
            elif i==j:
                return 0 if m==1 else inf
            else:
                if m==1:
                    return dp(i,j,K)+prefix[j+1]-prefix[i]
                else:
                    res=min(dp(i, mid,1)+dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
                    return res
        res = dp(0,N-1,1)
        return res if res<inf else -1
                
