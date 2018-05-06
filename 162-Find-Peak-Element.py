class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            if len(nums)==1:
                return 0
            if len(nums)==2:
                if nums[0]>nums[1]:
                    return 0
                else:
                    return 1
        
        left, right = 1,len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            #0<left<=mid<right<=len(nums)-1
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
                
        # stop at left = right
        if left ==len(nums)-1:
            if nums[left]>nums[left-1]:
                return left
        elif nums[left-1]<nums[left]>nums[left+1]:
            return left
        if nums[0]>nums[1]:
            return 0