class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        minM = float('inf')
        for i in range(1,len(stones)-1):
            loc = bisect.bisect_left(stones, stones[i]+len(stones)-1, lo=0, hi=len(stones)-1)
            if stones[loc] == stones[i]+len(stones)-1:
                minM = min(minM,len(stones)-(loc-i)-1)
            else:
                minM = min(minM,len(stones)-loc+i)
        if stones[-1]-stones[0]+1 == len(stones):
            minM = 0
        maxM = max(stones[-2]-stones[0]-len(stones)+2,stones[-1]-stones[1]-len(stones)+2)
        return [minM,maxM]
