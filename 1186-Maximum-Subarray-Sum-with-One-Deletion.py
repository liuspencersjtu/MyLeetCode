class Solution:
    def maximumSum(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:return A[0]
        res = max(A)
        inf = float('inf')
        left, right = [-inf]*n, [-inf]*n
        prefix, minPrefix = 0, 0
        for i, a in enumerate(A):
            prefix += a
            res = max(res, prefix-minPrefix)
            left[i] = prefix-minPrefix
            minPrefix = min(minPrefix, prefix)
        prefix, minPrefix = 0, 0
        for i in range(n-1,-1,-1):
            a = A[i]
            prefix += a
            right[i] = prefix-minPrefix
            minPrefix = min(minPrefix, prefix)
            res = max(res, (left[i-1] if i>0 else 0) + (right[i+1] if i<n-1 else 0))
        return res
