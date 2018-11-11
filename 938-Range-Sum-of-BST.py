# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def preorder(root):
            if not root:
                return []
            if root.val<L:
                if not root.right:
                    return []
                else:
                    return preorder(root.right)
            if root.val>R:
                if not root.left:
                    return []
                else:
                    return preorder(root.left)
            return preorder(root.left)+[root.val]+preorder(root.right)
        res = preorder(root)
        return sum(res)
        