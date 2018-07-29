# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_leaf(root):
            if not root:
                return False
            if not root.left and not root.right:
                return True
            else:
                return False
        if not root or is_leaf(root):
            return 0
        self.ans = 0
        def help(root):
            if not root:
                return
            if is_leaf(root.left):
                print(root.left.val)
                self.ans += root.left.val
            help(root.left)
            help(root.right)
        help(root)
        return self.ans