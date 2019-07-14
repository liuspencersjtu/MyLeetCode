import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        memo = collections.defaultdict(int)
        for it in arr1:
            memo[it]+=1
        res = []
        for it in arr2:
            res += [it]*memo[it]
            memo.pop(it)
        for it in sorted(memo.keys()):
            res += [it]*memo[it]
        return res
