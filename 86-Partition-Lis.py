# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 双dummy指针的方案比方案2更intuitive
        dummy1 = ListNode()
        dummy2 = ListNode()
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val<x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = dummy2.next
        return dummy1.next
        
    def partition(self, head: ListNode, x: int) -> ListNode:
        sentinel = ListNode(-300, head)
        prev = sentinel
        curr = sentinel
        while curr:
            while curr.next and curr.next.val < x:
                tmp = curr.next
                curr.next = curr.next.next
                tmp.next = prev.next
                prev.next = tmp
                # handle this corner case is kind of tricky,
                # the intuition is that, we want to cut the node behind curr
                # and connected it behind prev, but if prev==curr,
                # then the connect op will undo the disconnect
                # so we need to undo that
                if prev == curr:
                    curr = curr.next
                prev = prev.next
            curr = curr.next

        return sentinel.next
            
