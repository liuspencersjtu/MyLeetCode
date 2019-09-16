class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        prefix = arr*2
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        curmin = 0
        res = 0
        for a in prefix:
            res = max(res, a - curmin)
            curmin = min(a, curmin)
        singlesum = sum(arr)
        prefix2 = arr*1
        for i in range(len(prefix2)-1,0,-1):
            prefix2[i-1] += prefix2[i]
        if singlesum > 0:
            if k>=2:
                res = max(res, singlesum*(k-2) + max(prefix[:len(prefix)//2]) + max(prefix2))
            else:
                res = max(0, max(prefix[:len(prefix)//2]), max(prefix2))
        return res%(10**9+7)
