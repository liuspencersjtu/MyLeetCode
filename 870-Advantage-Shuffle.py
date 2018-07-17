class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        A = list(sorted(A))
        b = [(v, i) for i, v in enumerate(B)]
        b.sort()
        r = [-1] * n
        used = [False] * n
        i = 0
        for v, j in b:
            while i < n and A[i] <= v:
                i += 1
            if i < n:
                r[j] = A[i]
                used[i] = True
                i += 1
        i = 0
        for j in range(n):
            if used[j]: continue
            while r[i] >=0:
                i += 1
            r[i] = A[j]
            i += 1
        return r