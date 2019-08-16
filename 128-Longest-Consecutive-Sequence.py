class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num -1 not in nums:
                y = num + 1
                while y in nums:
                    y+=1
                res = max(res, y-num)
        return res
        
