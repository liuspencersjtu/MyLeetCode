# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        L = 1
        i = 0
        p = head
        if not p:
            return p
        while p.next:
            p = p.next
            L += 1
        tail = p
        p = head
        k = k%L
        k = L-k
        while i<k-1:
            if p.next:
                p = p.next
                i += 1
                # L += 1
            else:
                p = head
                i += 1
        if not p.next:
            return head
        else:
            tail.next = head
            head = p.next
            p.next = None
            return head
