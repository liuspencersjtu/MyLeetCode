# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        isCycle = False
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                isCycle = True
                break
        if not isCycle:
            return None
        p2 = head
        while p2!=p1:
            p2 = p2.next
            p1 = p1.next
        return p1
