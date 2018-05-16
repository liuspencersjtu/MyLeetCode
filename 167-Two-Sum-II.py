class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # binary search so the complexity is O(nlgn)
        def binarySearch(nums,tar):
            left = 0
            right = len(nums)-1
            while left<=right:
                mid=(left+right)//2
                #0<=left<=mid<=right<=len(nums)-1
                if nums[mid] == tar:
                    return nums[mid]
                if nums[mid]<tar:
                    left = mid+1
                else:
                    right = mid-1
            return None
                    
        for i in range(len(numbers)):
            if i>1 and numbers[i] == numbers[i-1]:
                continue
            val = binarySearch(numbers[:i]+numbers[i+1:],target-numbers[i])
            if val != None:
                if numbers.index(val) != i:
                    return [i+1,numbers.index(val)+1]
                return [i+1,numbers.index(val,i+1)+1]