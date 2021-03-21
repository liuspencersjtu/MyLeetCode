# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        prev = head
        curr = head.next
        while curr:
            if curr.val==val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        if head.val == val:
            return head.next
        else:
            return head
