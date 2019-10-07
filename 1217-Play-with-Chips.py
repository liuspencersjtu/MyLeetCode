class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        memo = collections.defaultdict(int)
        for chip in chips:
            memo[chip%2]+=1
        return min(memo[0],memo[1])
