import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-it for it in stones]
        heapq.heapify(res)
        while len(res)>1:
            a = heapq.heappop(res)
            b = heapq.heappop(res)
            if a==b:
                continue
            else:
                heapq.heappush(res,-abs(a-b))
        if not res:
            return 0 
        return abs(res[0])
        
