# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head
        #temp = head.val
        p = head
        while p.next!=None:
            if p.next.val == p.val:
                if p.next.next!= None:
                    p.next = p.next.next
                else:
                    p.next = None
            else:
                p = p.next
        return head
