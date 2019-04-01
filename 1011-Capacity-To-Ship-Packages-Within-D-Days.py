class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def greedy(A, vol):
            cur = 0
            res = 0
            for it in A:
                if cur+it>vol:
                    res+=1
                    cur=it
                else:
                    cur+=it
            res += 1
            return res
        vol = max(max(weights),sum(weights)//D)
        while greedy(weights,vol)>D:
            vol+=1
        return vol
