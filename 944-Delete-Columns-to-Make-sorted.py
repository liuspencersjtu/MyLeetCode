class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A)<2:
            return 0
        def helper(nums):
            if len(nums)<2:
                return True
            if nums[0]==nums[1]:
                return helper(nums[1:])
            elif nums[0]<nums[1]:
                # ascending
                mark = 0
                for i in range(1,len(nums)):
                    if nums[i]<nums[i-1]:
                        return False
                return True
            elif nums[0]>nums[1]:
                return False
                '''
                mark = 1
                for i in range(1,len(nums)):
                    if nums[i]>nums[i-1]:
                        return False
                return True
                '''
        B=[]
        for item in A:
            B.append([ord(i) for i in item])
        C=zip(*B)
        res = 0
        for item in C:
            if not helper(item):
                res +=1
        return res
                    
            