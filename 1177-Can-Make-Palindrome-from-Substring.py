import math, itertools
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        h = [0]
        for c in s: h.append(h[-1] ^ (1 << (ord(c) - ord('a'))))
        r = []
        for left, right, k in queries:
            v = h[right+1] ^ h[left]
            m = 0
            while v:
                v ^= v & -v
                m += 1
            r.append(m // 2 <= k)
        return r
