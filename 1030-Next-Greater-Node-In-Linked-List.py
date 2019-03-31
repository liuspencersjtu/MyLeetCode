# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from functools import lru_cache
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # return the next_larger node of A
        @lru_cache()
        def helper(A):
            B = A.next
            while B != None and B.val<=A.val:
                B = helper(B)
            ##
            if B==None:
                A.next_larger = 0
                return None
            else:
                A.next_larger = B.val
                return B
        tmp = head
        while tmp:
            helper(tmp)
            ##
            tmp = helper(tmp)
        res = []
        tmp = head
        while tmp:
            res.append(tmp.next_larger)
            tmp=tmp.next
        return res
