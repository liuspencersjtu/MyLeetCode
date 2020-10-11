class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        from itertools import combinations
        memo = defaultdict(int)
        for inode, onode in roads:
            memo[inode] += 1
            memo[onode] += 1
        res = 0
        connections = set((x,y) for x,y in roads)
        connections |= set((y,x) for x,y in roads)
        for inode, onode in combinations(list(range(n)),2):
            if (inode,onode) in connections:
                res = max(res, memo[inode]+memo[onode]-1)
            else:
                res = max(res, memo[inode]+memo[onode])
        return res
