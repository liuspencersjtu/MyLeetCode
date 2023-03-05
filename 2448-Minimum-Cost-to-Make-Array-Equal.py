class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # total = sum[ abs(nums[i]-target)*cost[i] ]
        # target from min(nums) to max(nums)
        # convex optmization
        # binary search for target
        def totalcost(target):
            return sum([abs(nums[i]-target)*cost[i] for i in range(len(nums))])

        l = left = min(nums)
        r = right = max(nums)
        while left<right:
            mid = (left+right)//2
            if totalcost(mid)<totalcost(mid+1):
                right = mid
            else:
                left = mid+1
        return totalcost(left)
        
