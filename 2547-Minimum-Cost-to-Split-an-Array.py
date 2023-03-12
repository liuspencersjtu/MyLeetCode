class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # dp[i] = min dp[j] + trimmed(nums[j:i]) + k for j in range(i)
        # 
        dp = [float('inf')]*(1+len(nums))
        dp[0] = 0
        for i in range(1,len(nums)+1):
            cnt = 0
            seen = defaultdict(int)
            for j in range(i-1,-1,-1): # 从后往前
                if seen[nums[j]]==0:
                    cnt += 1
                elif seen[nums[j]]==1:
                    cnt -= 1
                seen[nums[j]] += 1
                dp[i] = min(dp[i], dp[j] + (i-j) -cnt + k)
        
        return dp[-1]
