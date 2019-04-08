# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        even = head
        oddnode = ListNode(1)
        odd = oddnode
        preveven = head
        while even.next !=None:
            odd.next = even.next
            odd = odd.next
            if odd.next == None:
                even.next = oddnode.next
                return head
            print(even.val,odd.val)
            even.next = odd.next
            even = even.next
        odd.next = None
        even.next = oddnode.next
        return head
        
