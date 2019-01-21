# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(root):
            if not root:
                return 1
            left=helper(root.left)
            right=helper(root.right)
            val=root.val+left+right-2
            self.res+=abs(left-1)+abs(right-1)
            return val
        helper(root)
        return self.res
