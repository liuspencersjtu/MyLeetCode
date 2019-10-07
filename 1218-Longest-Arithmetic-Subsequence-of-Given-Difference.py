class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N = len(arr)
        dp = [1]*N
        res = 0
        memo = collections.defaultdict(int)
        for i in range(N):
            # for j in range(i):
            #     if arr[j]+difference==arr[i]:
            #         dp[i] = max(dp[j]+1,dp[i])
            dp[i] = max(dp[i], dp[i]+memo[arr[i]-difference])
            memo[arr[i]] = max(memo[arr[i]], dp[i])
            res = max(res, dp[i])
        # print(dp)
        return res
