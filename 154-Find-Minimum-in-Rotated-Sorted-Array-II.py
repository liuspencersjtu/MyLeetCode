class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        start, end = 0, len(nums) - 1
        while start<end:
            mid = (start+end)//2
            if nums[mid]>nums[end]:
                start = mid+1
            elif nums[mid]<nums[end]:
                end = mid
            else:
                end = end - 1
        return nums[start]

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0],nums[1])
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left + right)//2
            #0<=left<=mid<right<=len(nums)-1
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                #print(left,mid,right)
                a = nums[left:mid+1]
                b = nums[mid:right+1]
                return min(self.findMin(a),self.findMin(b))
            if nums[mid]<=nums[right]:
                right = mid
            else:
                left = mid + 1
                
        #stop at left == right 
        #if nums[left] == nums[0]:
        #print(left,right)
        return nums[0]