# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This is my answer

#class Solution(object):
#    def getIntersectionNode(self, headA, headB):
#        """
#        :type head1, head1: ListNode
#        :rtype: ListNode
#        """
'''        tag1 = 0
        #tag2 = 0
        pheadA = headA
        pheadB = headB
        #if headA == None or headB == None:
        #    return None
        while pheadA != pheadB:
            #pheadA = pheadA.next if pheadA != None else headB
            if pheadA != None:
                pheadA = pheadA.next
            else:
                pheadA = headB
                tag1 += 1
                if tag1 == 2:
                    return None
            pheadB = pheadB.next if pheadB != None else headA
'''
'''
            if pheadB != None:
                pheadB = pheadB.next
            else:
                pheadB = headA
                tag2 += 1
                if tag2 == 2:
                    return None
'''
'''        return pheadA
'''

#This is one of the fastest answer
class Solution(object):
    '''
    def getLen(self,head):
        counter = 0
        while head:
            counter += 1
            head = head.next
            
        return counter
    
    def getNewHead(self,head,idx):
        counter = 0
        
        while counter < idx:
            head = head.next
            counter += 1
        
        return head
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)
        
        if lenA > lenB:
            idxA = lenA - lenB
            nodeA = self.getNewHead(headA,idxA)
            nodeB = headB
        else:
            idxB = lenB - lenA
            nodeB = self.getNewHead(headB,idxB)
            nodeA = headA
        
        
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        else:
            return
        '''
    def getIntersectionNode(self, headA, headB):
        trav_a, trav_b = headA, headB
        while trav_a is not trav_b:
            trav_a = headB if not trav_a else trav_a.next
            trav_b = headA if not trav_b else trav_b.next
        return trav_a