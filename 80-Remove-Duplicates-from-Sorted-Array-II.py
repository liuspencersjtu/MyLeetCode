class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import defaultdict
        memo = defaultdict(int)
        slow = 0
        for fast, num in enumerate(nums):
            if memo[num]==2:
                continue
            else:
                memo[num] += 1
                nums[slow] = nums[fast]
                slow += 1
        return slow
