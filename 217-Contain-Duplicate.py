class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        dic={}
        for i in nums:
            dic[i] = dic.get(i,0)+1
            
        for i in dic.values():
            if i > 1:
                return True
        return False
        '''
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False