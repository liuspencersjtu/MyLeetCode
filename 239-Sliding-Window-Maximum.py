class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # using deque to restore key points
        # idealy we can store k numbers,
        # but to make find the maximun at cost O(1)
        # we can keep the stored number in a descending order
        deque = []
        for i in range(len(nums)):
            while deque and nums[i]>nums[deque[-1]]:
                deque.pop()
            if deque and deque[0]<=i-k:
                deque.pop(0)
            deque.append(i)
            if i>=k-1:
                res.append(nums[deque[0]])
        return res
