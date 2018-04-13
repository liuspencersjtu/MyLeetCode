class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = []
        n = len(nums)
        for i in range(n):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(n):
            output[n-1-i] *= p
            p *= nums[n-1-i]
        return output