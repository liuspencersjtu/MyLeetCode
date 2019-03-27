import heapq
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        curr = 1
        while nums and nums[0]<=0:
            heapq.heappop(nums)
        while nums:
            ##
            a = heapq.heappop(nums)
            while nums and nums[0]==a:
                heapq.heappop(nums)
            if a!=curr:
                return curr
            curr+=1
        return curr
