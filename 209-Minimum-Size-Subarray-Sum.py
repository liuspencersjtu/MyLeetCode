class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = nums[0]
        low, fast = 0, 0
        res = float('inf')
        while 0<=low<=fast<len(nums):
            while curr>=target and low<=fast:   
                res = min(res, fast-low+1)
                curr -= nums[low]
                low += 1
            # extreme case low=fast+1, curr=0
            while curr<target:
                fast += 1
                if fast>=len(nums):
                    break
                else:
                    curr += nums[fast]
        if res<float('inf'):
            return res
        else:
            return 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import sys
        start, end, sums, res = 0, 0, 0, sys.maxsize
        while end < len(nums):
            sums += nums[end] 
            end += 1 #先操作再移动指针
            while sums >= target:
                sums -= nums[start]
                start += 1
                res = min(res, end-start+1)
        return res if res != sys.maxsize else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            sums[i] = sums[i-s] + nums[i-1] # sum of first i elements
        for i in range(1, len(nums)+1):
            to_find = target + sums[i-1] # minimum subarray starting from index i to have sum greater than target
            idx = bisect.bisect_left(sums, to_find)
            if idx != len(sums):
                res = min(res, idx-i+1)
        return res if res != sys.maxsize else 0
