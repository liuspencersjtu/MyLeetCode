class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        memo = collections.defaultdict(int)
        def helper(i):
            if i:
                return 0
            else:
                return 1
        for it in matrix:
            if it[0]==0:
                memo[tuple(it)]+=1
            else:
                memo[tuple(helper(i) for i in it)]+=1
        return max(memo.values())
