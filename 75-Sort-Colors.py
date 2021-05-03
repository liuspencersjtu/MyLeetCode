class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        memo = {0:0,1:0,2:0}
        for num in nums:
            memo[num] += 1
        for i in range(0, memo[0]):
            nums[i] = 0
        for i in range(memo[0], memo[0]+memo[1]):
            nums[i] = 1
        for i in range(memo[0]+memo[1], memo[0]+memo[1]+memo[2]):
            nums[i] = 2
