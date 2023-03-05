class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # record the best k consecutive sum in the first i elements
        dp = [0]*(len(prizePositions)+1)
        res = 0
        j = 0
        for i, prize in enumerate(prizePositions):
            while prizePositions[j]<prize-k:
                j += 1
            dp[i+1] = max(dp[i], i-j+1)#here dp[i] include items till i-1
            res = max(res, dp[j]+i-j+1)
        return res
