from collections import defaultdict
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        memo = defaultdict(int)
        for i in barcodes:
            memo[i]+=1
        i = 0
        N = len(barcodes)
        res = []
        for _ in range(N):
            res.append(0)
        for n, x in sorted([v,k] for k, v in memo.items())[::-1]:
            for _ in range(n):
                if i<N:
                    res[i]=x
                    i+=2
                else:
                    i=1
                    res[i]=x
                    i+=2
        return res
