# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return []
        heap = []
        memo = collections.defaultdict(list)
        for it in lists:
            if it:
                heap.append(it.val)
                memo[it.val].append(it)
        heapq.heapify(heap)
        res = []
        while heap:
            ##
            val = heapq.heappop(heap)
            it = memo[val].pop()
            res.append(val)
            if it.next:
                heapq.heappush(heap,it.next.val)
                memo[it.next.val].append(it.next)
        return res
