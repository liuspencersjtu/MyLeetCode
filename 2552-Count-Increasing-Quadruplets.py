class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # dp loop for j to find 132 in value
        # store # of previous small
        # 
        n = len(nums)
        ans = 0
        dp = [0]*n
        prev_small = [0]*n
        for j in range(n):
            # prev_small = 0
            for i in range(j): #i<j
                if nums[i]<nums[j]:
                    prev_small[j] += 1
                    ans += dp[i]
                if nums[i]>nums[j]:
                    dp[i] += prev_small[j]
        return ans
                
