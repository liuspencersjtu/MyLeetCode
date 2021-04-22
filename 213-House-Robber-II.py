class Solution:
    def rob(self, nums: List[int]) -> int:
        # 思路是这样，因为间隔里最多有两个房子没有偷
        # 反证之，如果连着3个没有偷，那加上中间这一个肯定比目前的结果更多
        # 假设房子水平的偷法为rob_no_circle
        # 那么不偷0，只需要计算剩下的rob_no_circle(nums[1:])
        # 如果偷了0，那么需要计算rob_no_circle(nums[2:len(nums)-1])
        # rob_no_circle就是一个标准dp问题了，或者说贪心问题(a_n = max(a_n-1, a_n-2+val_n))
        def rob_no_circle(nums):
            if not nums:
                return 0
            if len(nums)==1:
                return nums[0]
            if len(nums)==2:
                return max(nums)
            # return max(rob_no_circle(nums[:-1]), rob_no_circle(nums[:-2]+nums[-1])
            a1,a2 = nums[0], max(nums[:2])
            for i in range(2,len(nums)):
                res = max(a1+nums[i],a2)
                a1 = a2
                a2 = res
            return res
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        return max(rob_no_circle(nums[1:]),rob_no_circle(nums[2:len(nums)-1])+nums[0])
