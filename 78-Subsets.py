class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]+[[]]
        else:
            k = self.subsets(nums[1:])
            res = [[nums[0]]]+[[nums[0]]+ item for item in k if item != []]+[i for i in k if i != []]
            return res+[[]]
            