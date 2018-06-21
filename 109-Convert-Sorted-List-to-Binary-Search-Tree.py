# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l = []
        h = head
        #print(h.val)
        while h != None:
            l.append(h.val)
            h = h.next
        def toBST(l):
            #print('Start')
            if not l:
                return None
            mid = len(l)//2
            t = TreeNode(l[mid])
            t.left = toBST(l[:mid])
            t.right = toBST(l[mid+1:])
            return t
        return toBST(l)