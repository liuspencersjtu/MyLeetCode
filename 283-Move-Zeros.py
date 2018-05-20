class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        l = len(nums)
        while right< l and nums[right] != 0:
            right += 1
        while right < l and left < l:
            while right < l and nums[right] == 0:
                if right < l:
                    right += 1
            while left <= right and nums[left] != 0:
                if left < l:
                    left += 1
            #stop where right is non-0 and left is 0
            if left != l  and right != l:
                nums[left], nums[right] = nums[right], nums[left]
        