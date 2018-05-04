class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums)<=2:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            print(mid)
            if nums[mid] == target:
                return mid
            
            if nums[left]<nums[right]:
                if nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]>=nums[left]:
                    if target>=nums[mid]:
                        left = mid+1
                    elif target>=nums[left]:
                        right = mid-1
                    else:
                        left = mid+1
                else:
                    if target<=nums[mid]:
                        right = mid-1
                    elif target<=nums[right]:
                        left = mid+1
                    else:
                        right = mid-1
                
        
        if nums[0] == target:
            return 0
        if nums[len(nums)-1] == target:
            return len(nums)-1
        
        # left>right
        return -1