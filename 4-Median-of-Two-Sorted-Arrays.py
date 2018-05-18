class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def median(array):
            l = len(array)
            if l%2 == 1:
                return array[l//2]
            else:
                return (array[l//2]+array[l//2-1])/2
            
        if len(nums1)<len(nums2):
            nums1, nums2 = nums2, nums1
        
        if not nums2:
            return median(nums1)
        if nums1[-1]<=nums2[0]:
            return median(nums1+nums2)
        if nums2[-1]<=nums1[0]:
            return median(nums2+nums1)
        
        length = len(nums1)+len(nums2)
        # We got nums1 no shorter than number nums2, so we search nums2
        left = 0
        right = len(nums2)-1
        l = (len(nums1)+len(nums2)+1)//2
        # get the middle or the exact left of middle
        while left <= right:
            #print(left,right)
            mid = (left+right)//2
            #0<=left<=mid<=right<=len(nums2)-1
            mid2 = l - (mid+1) - 1
            print(mid,mid2)
            if mid == len(nums2)-1:
                if nums2[mid]<=nums1[mid2+1]:
                    if length%2 == 1:
                        return max(nums2[mid],nums1[mid2])
                    else:
                        return (max(nums2[mid],nums1[mid2])+nums1[mid2+1])/2
                
            elif mid2 == len(nums1) - 1:
                if nums1[mid2]<=nums2[mid+1]:
                    if length%2 == 1:
                        return max(nums2[mid],nums1[mid2])
                    else:
                        return (max(nums2[mid],nums1[mid2])+nums2[mid+1])/2
            
            if nums2[mid]<=nums1[mid2+1] and nums1[mid2]<= nums2[mid+1]:
                if length%2 ==1:
                    return max(nums2[mid],nums1[mid2])
                else:
                    return (max(nums2[mid],nums1[mid2])+min(nums1[mid2+1],nums2[mid+1]))/2
            else:
                if nums2[mid]>nums1[mid2]:
                    right = mid -1
                else:
                    left = mid +1
                    
        if right == -1 or left == -1:
            mid2 = l - 1
            if length%2 == 1:
                return nums1[mid2]
            else:
                return (nums1[mid2]+min(nums1[mid2+1],nums2[0]))/2
        elif left == len(nums2) or right == len(nums2):
            mid2 = l -len(nums2) - 1
            if length%2 == 1:
                return max(nums1[mid2],nums2[-1])
            else:
                return (max(nums1[mid2],nums2[-1])+nums1[mid2+1])/2