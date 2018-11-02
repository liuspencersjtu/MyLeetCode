# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1,n2=[],[]
        while l1 != None:
            n1.insert(0,str(l1.val))
            l1=l1.next
        while l2 != None:
            n2.insert(0,str(l2.val))
            l2=l2.next
        n1=int(''.join(n1))
        n2=int(''.join(n2))
        n3=str(n1+n2)
        l = None
        for i in n3:
            temp=ListNode(i)
            temp.next=l
            l=temp
        return l