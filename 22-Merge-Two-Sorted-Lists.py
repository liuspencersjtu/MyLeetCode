# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        node = ListNode(0)
        res = node
        while (p1 or p2):
            if not p1:
                res.next = ListNode(p2.val)
                res=res.next
                p2 = p2.next
            elif not p2:
                res.next = ListNode(p1.val)
                res=res.next
                p1 = p1.next
            else:
                if p1.val<=p2.val:
                    res.next = ListNode(p1.val)
                    res = res.next
                    p1=p1.next
                else:
                    res.next = ListNode(p2.val)
                    res = res.next
                    p2=p2.next
        return node.next
