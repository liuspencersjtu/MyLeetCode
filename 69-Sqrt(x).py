class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        
        while left <= right:
            mid = (left+right)//2
            if mid*mid == x:
                return mid
            elif mid*mid >x:
                right = mid-1
            else:
                left = mid+1
                
        #end at left>right
        if left*left<=x:
            return left
        else:
            return right