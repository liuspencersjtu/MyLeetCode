# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, nsum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        res = False
        def check(root,pathsum):
            nonlocal res
            if root.left == None and root.right == None:
                if (pathsum + root.val) == nsum:
                    res = True
            else:
                pathsum += root.val
                if root.left:
                    check(root.left, pathsum)
                if root.right:
                    check(root.right, pathsum)
                
        check(root, 0)
        return res