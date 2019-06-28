# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cnt = n+1
        tmp = ListNode(0)
        tmp.next=head
        p1,p2=tmp,tmp
        while p2!=None:
            if cnt:
                p2 = p2.next
                cnt-=1
            else:
                p2=p2.next
                p1=p1.next
        if p1.next==None:
            return None
        else:
            p1.next=p1.next.next
            return tmp.next
