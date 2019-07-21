from functools import lru_cache
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(4096)
        def helper(i,j):
            if i==j:
                return 0, arr[i]
            res = float('inf')
            for mid in range(i,j):
                tmp1, left = helper(i,mid)
                tmp2, right = helper(mid+1,j)
                res = min(res,left*right+tmp1+tmp2)
            return res, max(arr[i:j+1])
        return helper(0,len(arr)-1)[0]
