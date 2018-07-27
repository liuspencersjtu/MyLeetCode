# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        else:
            if root.val>val:
                root.left = self.insertIntoBST(root.left, val)
                return root
            else:
                root.right = self.insertIntoBST(root.right, val)
                return root