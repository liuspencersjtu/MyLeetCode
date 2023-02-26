class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        i, j = 0, len(nums)//2 # here the selection of j is critical
                               # becase we know at most there will be len(nums)//2 paris
                               # and avoid select some pairs with both elements in first
                               # half.
        N = len(nums)
        res = 0
        while j<len(nums) and i<N//2:
            # while i<N and i in marked:
            #     i += 1
            if nums[j]>=2*nums[i]:
                i += 1
                res += 2
            j += 1
        return res
