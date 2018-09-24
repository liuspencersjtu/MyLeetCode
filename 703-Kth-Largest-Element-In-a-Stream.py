class KthLargest:
	# 最后还是用了python写好的堆来实现.....代码来自于@cnkyzz@leetcode
	def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        self.size = len(self.pool)
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums)>k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) <self.k:
            heapq.heappush(self.nums, val)
        elif val>self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)