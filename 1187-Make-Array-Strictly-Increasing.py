class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        B = sorted(list(set(B)))
        n, m = len(A), len(B)
        cur = {0:-1}
        res = 0
        inf = float('inf')
        for a in A:
            cur2 = {}
            for k in cur:
                if cur[k] < a:
                    cur2[k] = min(cur2.get(k, inf), a)
                i = bisect.bisect(B,cur[k])
                if i < m and B[i] != a:
                    cur2[k+1] = min(cur2.get(k+1, inf), B[i])
            cur = cur2
            if len(cur2) == 0:
                return -1
        # print(cur)
        return min(cur)
