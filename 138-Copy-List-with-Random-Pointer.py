# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        res = RandomListNode(0)
        cur = res
        p1 = head
        memo = {}
        while p1:
            cur.next = RandomListNode(p1.label)
            cur.next.random = p1.random
            memo[p1]=cur.next
            p1 = p1.next
            cur = cur.next
        p1 = head
        cur = res
        while cur.next:
            if cur.next.random:
                cur.next.random = memo[cur.next.random]
            cur = cur.next
        #print(res.label,res.next.label)
        return res.next
