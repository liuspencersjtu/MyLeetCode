class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums)==1:
            return len(nums)
        length = 1
        while length<len(nums):
            if nums[length]==nums[length-1]:
                nums.pop(length)
            else:
                length+=1
        return length
