class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=3:
            p,q,q1 = 0,0,0
            while q < len(nums):
                if nums[p] != target:
                    p += 1
                    q += 1
                else:
                    if nums[q] == target:
                        q1 = q
                        q += 1
                    else:
                        q += 1
            if p == len(nums):
                return [-1,-1]
            else:
                return [p,q1]
            
        left, right = 0,len(nums)-1
        
        while left+1<right:
            mid = (left+right)//2
            #print(left,right)
            #0<=left<mid<right<=len(nums)-1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if right == 1:
            if nums[left] == target:
                right = left
        l = right
        
        left, right = 0,len(nums)-1
        while left+1<right:
            mid = (left+right)//2
            #print(left,right)
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        if left+1 == len(nums)-1:
            if nums[right] == target:
                left = right
        r = left
        
        print(l,r)
        
        if l<=r:
            return [l,r]
        else:
            return [-1,-1]