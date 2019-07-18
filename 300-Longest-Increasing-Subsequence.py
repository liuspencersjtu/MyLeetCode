class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # classic dp problem
        # https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
        if not nums:
            return 0
        N = len(nums)
        memo = [0]*N
        for i in range(N):
            localmax = 1
            for j in range(i):
                if nums[i]>nums[j] and localmax<memo[j]+1:
                    localmax = memo[j]+1
            memo[i] = localmax
        return max(memo)
