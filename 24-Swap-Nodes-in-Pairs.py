# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cnt = 0
        node = ListNode(0)
        node.next=head
        p0 = node
        p1 = head
        p2 = head.next
        while p2 != None:
            #
            if cnt %2 == 0:
                p0.next = p2
                p1.next = p2.next
                p2.next = p1
                p1, p2 = p2, p1
            #
            p0 = p1
            p1 = p2
            p2 = p2.next
            cnt+=1
        return node.next
