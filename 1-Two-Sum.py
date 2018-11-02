class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = list(enumerate(nums))
        def return2(nums):
            return nums[1]
        nums.sort(key=return2)
        p1,p2=0,len(nums)-1
        while p1!=p2:
            n = nums[p1][1]+nums[p2][1]
            if n==target:
                return [nums[p1][0],nums[p2][0]]
            elif n>target:
                p2-=1
            else:
                p1+=1
        return