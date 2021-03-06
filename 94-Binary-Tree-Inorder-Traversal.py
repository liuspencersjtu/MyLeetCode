# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)