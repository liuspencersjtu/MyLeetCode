class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {1:cost[0],2:cost[1]}
        def dp(i):
            if i in memo:
                return memo[i]
            res = min(cost[i-1]+dp(i-1), cost[i-1]+dp(i-2))
            memo[i] = res
            return res
        cost.append(0)
        return dp(len(cost))
