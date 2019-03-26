import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = collections.defaultdict(int)
        for it in nums:
            memo[it]+=1
        tmp = []
        for it in memo:
            heapq.heappush(tmp,(-memo[it],it))
        res = []
        while k>0:
            res.append(heapq.heappop(tmp)[1])
            k-=1
        return res
