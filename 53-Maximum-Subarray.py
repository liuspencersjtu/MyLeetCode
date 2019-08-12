class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cur = 0
        prefix = []
        for it in nums:
            cur += it
            prefix.append(cur)
        memo = []
        gap = -float('inf')
        curmin = 0
        prefix.insert(0,0)
        for i in range(1,len(prefix)):
            tmp = prefix[i]-prefix[curmin]
            if tmp>gap:
                memo.append([tmp,curmin,i])
                gap = tmp
            if prefix[i]<prefix[curmin]:
                curmin = i
        # print the index range a..b
        # print(max(memo)[1:])
        return max(memo)[0]
