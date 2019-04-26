# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=''
        s2=''
        a=l1
        b=l2
        while(a or b):
            if(a):
                s1+=str(a.val)
                a=a.next
            if(b):
                s2+=str(b.val)
                b=b.next
        sum=str(int(s1)+int(s2))
        head=None
        for i in range(len(sum)-1,-1,-1):
            if(head==None):
                head=ListNode((sum[i]))
            else:
                temp=ListNode((sum[i]))
                temp.next=head
                head=temp
        return head
