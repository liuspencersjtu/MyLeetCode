class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def helperodd(nums):
            # odd is higher
            res = 0
            N = len(nums)
            for i in range(0,N,2):
                if i>0 and nums[i]>=nums[i-1]:
                    res += nums[i]-nums[i-1]+1
                    nums[i] = nums[i-1]-1
                if i<N-1 and nums[i]>=nums[i+1]:
                    res += nums[i]-nums[i+1]+1
                    nums[i] = nums[i+1]-1
            return res
        def helpereven(nums):
            # odd is higher
            res = 0
            N = len(nums)
            for i in range(1,N,2):
                if i>0 and nums[i]>=nums[i-1]:
                    res += nums[i]-nums[i-1]+1
                    nums[i] = nums[i-1]-1
                if i<N-1 and nums[i]>=nums[i+1]:
                    res += nums[i]-nums[i+1]+1
                    nums[i] = nums[i+1]-1
            return res
        # print(helperodd(nums.copy()), helpereven(nums.copy()))
        return min(helperodd(nums.copy()), helpereven(nums.copy()))
