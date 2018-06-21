class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        maxlength = 0
        #res = []
        fast = 0
        #temp = []
        length = 0
        n = len(nums)-1
        while fast<n:
            if nums[fast]<nums[fast+1]:
                #temp.append(nums[fast])
                length += 1
                fast += 1
            else:
                #temp.append(nums[fast])
                length += 1
                # begin juding
                if length>maxlength:
                    #res = temp
                    maxlength = length
                #temp = []
                length = 0
                fast += 1
        if nums[n]>nums[n-1]:
            length += 1
        if length > maxlength:
            maxlength = length
                
        return maxlength