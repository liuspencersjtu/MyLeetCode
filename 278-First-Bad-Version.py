# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #preprocessing
        if n==1 and isBadVersion(1):
            return 1
                
        left, right = 1, n
        
        while left<right:
            mid = (left+right)//2 + 1
            # Which means left<mid<=right,thus mid-1>0
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid-1
                
        #postprocessing, stop at left==right
        if left == 1:
            if isBadVersion(1):
                return 1
        else:
            if isBadVersion(left) and not isBadVersion(left-1):
                return left
        