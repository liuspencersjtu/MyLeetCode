class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res=[]
        counter=0
        for i in range(len(nums)):
            if nums[i]!=1:
                res.append(counter)
                counter=0
            else:
                counter+=1
        res.append(counter)
        return max(res)