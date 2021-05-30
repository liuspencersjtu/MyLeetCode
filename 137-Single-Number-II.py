class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        memo = defaultdict(lambda :3)
        for it in nums:
            memo[it]-=1
            if memo[it]==0:
                memo.pop(it)
        return list(memo.keys())[0]
