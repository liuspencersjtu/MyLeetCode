class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        lo = min(nums)
        hi = max(nums)
        
        while(hi-lo)>1e-6:
            mid = (lo+hi)/2
            if self.ok(nums,k,mid):
                lo = mid
            else:
                hi = mid
        return hi
        
    def ok(self, nums, k, mid):
        t = [it-mid for it in nums]
        mysum1 = sum(t[:k])
        if mysum1>0:
            return True
        mymin = 0
        mysum2 = 0
        for i in range(k,len(t)):
            mysum2 += t[i-k]
            mysum1 += t[i]
            mymin = min(mymin,mysum2)
            if mysum1-mymin>=0:
                return True
        return False
