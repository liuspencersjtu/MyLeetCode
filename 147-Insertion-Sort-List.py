# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        length = 1
        dummy = ListNode(None, head)
        curr_prev = head
        curr = head.next
        while curr:
            prev = dummy
            p = dummy.next
            cnt = 0
            while p and p.val<curr.val and cnt<length:
                prev = p
                p = p.next
                cnt += 1
            if curr == p:
                length += 1
                curr_prev = curr
                curr = curr.next
                continue
            #break curr
            n = curr.next
            curr_prev.next = n
            #replace curr
            prev.next = curr
            curr.next = p
            #redefine curr
            curr = n
            length += 1
        
        res = []
        p = dummy.next
        # while p:
        #     res.append(p.val)
        #     p = p.next
        # print(dummy.next.next.next.next.val)
        return dummy.next
