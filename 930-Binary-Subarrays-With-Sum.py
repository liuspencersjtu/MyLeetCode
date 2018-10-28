class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        counter, pre_sum, res = collections.Counter(), 0, 0 
        counter[0] = 1
        for num in A:
            pre_sum += num 
            res += counter[pre_sum-S]
            counter[pre_sum] += 1
            
        return res 