# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        def dfs(root, level = 0):
            if not root:
                return level
            level += 1
            a = dfs(root.left, level)
            b = dfs(root.right, level)
            if abs(a-b) > 1:
                self.ans = False
            return max(a,b)
        dfs(root)
        return self.ans