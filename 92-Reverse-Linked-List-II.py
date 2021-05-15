# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        p = head
        sentinel = ListNode(next=head)
        prev = sentinel
        reverse = False
        cnt = 1
        if left == right:
            return head
        while True:
            if cnt == right+1:
                r1 = prev
                r2 = p
                l1.next = r1
                l2.next = r2
                cnt += 1
                break
            if cnt == left:
                l1 = prev
                l2 = p
                reverse = True
                prev, p = prev.next, p.next
                cnt += 1
                continue
            if reverse == True:
                tmp = p.next
                p.next = prev
                prev = p
                p = tmp
                cnt += 1
            else:
                prev, p = prev.next, p.next
                cnt += 1
        # 要return sentinel.next而不是head，这样可以覆盖到第一个数就被翻转的情况
        return sentinel.next
            
