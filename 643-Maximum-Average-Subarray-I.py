class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        presum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            presum[i+1]=presum[i]+nums[i]
        res = -float('inf')
        for i in range(k,len(presum)):
            res = max(res,presum[i]-presum[i-k])
        return res/k
