class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        else:
            res = []
            for i in range(len(nums)):
                res += [[nums[i]]+item for item in self.permute(nums[:i]+nums[i+1:])]
            return res