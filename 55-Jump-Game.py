class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        lst = [0]*(2*N)
        lst[N-1]=1
        for i in range(N-2,-1,-1):
            if nums[i]:
                lst[i]=max(lst[i+1:i+nums[i]+1])
        return bool(lst[0])
