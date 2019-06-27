class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            memo = set()
            res = []
            for it in nums:
                if target-it in memo:
                    res.append([it, target-it])
                else:
                    memo.add(it)
            #print(memo)
            return res
        def threeSum(nums, target):
            res = []
            for i in range(len(nums)):
                tmp = twoSum(nums[i+1:],target-nums[i])
                #print(tmp,nums[i],target-nums[i],nums[:i]+nums[i+1:])
                if tmp:
                    res+=[li + [nums[i]] for li in tmp]
            return res
        nums.sort()
        res = set()
        for i in range(len(nums)):
            tmp = threeSum(nums[i+1:],target-nums[i])
            if tmp:
                for li in tmp:
                    res.add(tuple(li + [nums[i]]))
        res = [list(it) for it in res]
        return res
        
