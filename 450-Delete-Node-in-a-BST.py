# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        p = root
        king = TreeNode(0)
        pupper = king
        pupper.left = root
        while True:
            if not p:
                return root
            if p.val == key:
                break
            elif p.val>key:
                pupper = p
                p = p.left
            else:
                pupper = p
                p = p.right
        if not p.left:
            if pupper.left == p:
                pupper.left = p.right
            else:
                pupper.right = p.right
        else:
            p2 = p.left
            p3 = p
            while (p2.right != None):
                p3 = p2
                p2 = p2.right
            p.val = p2.val
            if p3 != p:
                p3.right = p2.left
            else:
                p3.left = p2.left
            
        return king.left