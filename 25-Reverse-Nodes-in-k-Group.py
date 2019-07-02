# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        start = ListNode(0)
        start.next = head
        cnt = 1
        p1,p2 = start, start.next
        memo = []
        if k == 1:
            return head
        while p2 != None:
            if cnt == k:
                ##
                memo.append(p2)
                p1.next = p2
                memo[0].next = memo[-1].next
                for i in range(1,len(memo)):
                    memo[i].next=memo[i-1]
                p1 = memo[0]
                p2 = memo[0].next
                memo = []
                cnt = 1
            else:
                memo.append(p2)
                p2 = p2.next
                cnt += 1
        return start.next
