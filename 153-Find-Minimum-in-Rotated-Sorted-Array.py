class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        left, right = 1,len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            print nums[mid]
            #0<left<=mid<right<=len(nums)
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            #this is important,compare nums[mid]>nums[right]
            #rather than nums[mid]>=nums[left]
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
                
        # postprocessing
        # stop at left == right
        if left == 1:
            if nums[0]>nums[1]:
                return nums[1]
            else:
                return nums[0]
        return nums[left]
    
        '''
        def findMin(self, nums):
        l, r = 0, len(nums) -1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])
        '''
        '''
        Use l + 1 < r to finally choose out two elements to get the min number.
        The while loop is that when nums[mid] > nums[r], it means that min number is absolutely in the right half.
        Otherwise, the min number is the mid number or in the left half.
        Enjoy!
        '''
        