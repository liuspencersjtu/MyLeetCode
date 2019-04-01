class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        memo = collections.defaultdict(int)
        res = 0
        for i in range(len(time)):
            tmp = time[i]%60
            if tmp == 0:
                res += memo[tmp]
            elif 60-tmp in memo:
                res += memo[60-tmp]
            memo[tmp]+=1
        return res
