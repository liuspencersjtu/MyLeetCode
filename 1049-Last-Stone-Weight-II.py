class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ## knapsack problem
        ## dp to record achievable value in one knapsack
        ## sum-dp means value in the other knapsack
        ## their difference is the candidate value for the results
        dp={0}
        sumA = sum(stones)
        for a in stones:
            dp |= {a+i for i in dp}
        return min([abs(sumA-i - i) for i in dp])
    
    def lastStoneWeightIISolutionII(self, stones: List[int]) -> int:
        ## Lee215@Leetcode: Adapted dp to this problem.
        ## In this solution, I use dp to record the achievable diff of one group.
        ## If x in the set dp, it means the difference x is achievable currently.
        dp, sumA = {0}, sum(A)
        for a in A:
            dp = {a + x for x in dp} | {a - x for x in dp}
        return min(abs(x) for x in dp)
