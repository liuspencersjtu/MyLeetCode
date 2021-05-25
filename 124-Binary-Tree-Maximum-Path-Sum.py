# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(self.res, left+right+root.val, left+root.val, right+root.val, root.val)
            return max(root.val, root.val + max(left,right))
        rootpathsum = helper(root)
        # res = max(self.res, rootpathsum)
        return self.res
