class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        low, fast = 0, 0
        while fast<len(nums):
            if fast and nums[fast]-nums[fast-1]>1:
                if fast-low==1:
                    res.append(str(nums[low]))
                else:
                    res.append(str(nums[low])+'->'+str(nums[fast-1]))
                low = fast
            fast += 1
        if fast-low==1:
            res.append(str(nums[low]))
        else:
            res.append(str(nums[low])+'->'+str(nums[fast-1]))
        return res
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for i in range(len(nums)):
            if not res or nums[i]>res[-1][-1]+1:
                res.append([])
            if len(res[-1])<2:
                res[-1].append(nums[i])
            else:
                res[-1][1] = nums[i]
        return ['->'.join(map(str, r)) for r in res]
