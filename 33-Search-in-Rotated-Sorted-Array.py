class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
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
        
        # left>right
        return -1
        

        '''
        #Another solution
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
        '''
