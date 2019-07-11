import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


'''
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        N = len(nums)
        while left<right:
            mid = (left+right)//2
            # left<=mid<right
            if nums[mid]>=target:
                right = mid
            else:
                left = mid+1
        if right == N-1 and nums[right]<target:
            return N
        return right
            
'''
