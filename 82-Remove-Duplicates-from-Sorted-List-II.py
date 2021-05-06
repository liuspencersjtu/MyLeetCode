# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        if not head:
            return head
        while head and head.next and head.val == head.next.val:
            prev = head
            head = head.next
            while head and prev.val == head.val:
                head = head.next
                prev = prev.next
            
        while p:
            while p.next and p.next.next and p.next.next.val == p.next.val:
                while p.next and p.next.next and p.next.next.val == p.next.val:
                    p.next.next = p.next.next.next
                p.next = p.next.next
            p = p.next
        return head

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        prev = sentinel
        while head:
            if head.next and head.next.val == head.val:
                ##
                while head.next and head.next.val == head.val:
                    head.next = head.next.next
                prev.next = head.next
            else:
                prev = prev.next
            head = prev.next
        return sentinel.next
