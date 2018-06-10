class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        n = len(nums)
        for i in nums:
            if cnt.get(i,0) == 0:
                cnt[i] = 1
            else:
                cnt[i] += 1
                if cnt[i]> n//2:
                    return i
        if n == 1:
            return nums[0]

    #another solution
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        
        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)
        return candidate