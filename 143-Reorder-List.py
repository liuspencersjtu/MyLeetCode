# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        # p = stack.pop(0)
        # while stack:
        #     p.next = stack.pop()
        #     p = p.next
        #     if stack:
        #         p.next = stack.pop(0)
        #         p = p.next
        #     else:
        #         break
        p = stack[0]
        N = len(stack)
        for i in range(1, N//2+1):
            p.next = stack[N-i]
            p = p.next
            if N-i != i:
                p.next = stack[i]
                p = p.next
        p.next = None
        return head
