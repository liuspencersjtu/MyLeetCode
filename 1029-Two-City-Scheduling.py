from collections import defaultdict
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = list(map(lambda x: x[1]-x[0], costs))
        ans = sum(map(lambda x: x[0], costs))
        diff.sort()
        n = len(diff) // 2
        for i in range(n):
            ans += diff[i]
        return ans
