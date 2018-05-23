class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        memo = {}
        for i in nums:
            if memo.get(i,0) == 0:
                memo[i] = 1
            else:
                memo[i] += 1
        res = []
        for i in range(1,len(nums)+1):
            if memo.get(i,0) == 0:
                res.append(i)
                
        return res