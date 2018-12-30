# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        p = root.val
        q = [root]
        while q:
            item = q.pop(0)
            if item.val != p:
                return False
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
        return True
