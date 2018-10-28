class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        counter = Counter()
        base = 0
        p=[]
        for i in range(len(nums)):
            base+=nums[i]
            p.append(base)
        res=0
        p.insert(0,0)
        for i in p:
            res+=counter[i]
            counter[i+k]+=1
        return res