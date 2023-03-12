class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        bitmask = 0
        # prev = []
        prev = 0
        res = 0
        from collections import defaultdict
        mp = defaultdict(list)
        mp[0].append(-1)
        for j in range(len(nums)):
            prev ^= nums[j]
            res += len(mp[prev])
            mp[prev].append(j)
        return res
