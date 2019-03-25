class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cache = set()
        def twoSum(nums,a):
            memo = set()
            res = []
            for it in nums:
                if it in memo:
                    if (-a,a-it, it) not in cache:
                        res.append([-a,a-it, it])
                        memo.add(a-it)
                        cache.add((-a,a-it, it))
                        cache.add((-a,it,a-it))
                        cache.add((a-it,-a,it))
                        cache.add((a-it,it,-a))
                        cache.add((it,-a,a-it))
                        cache.add((it,a-it,-a))
                else:
                    memo.add(a-it)
            return res
        res = []
        for i in range(len(nums)):
            res += twoSum(nums[i+1:],-nums[i])
        return res
