# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        res = []
        while root and stack:
            res.append(stack[0].val)
            newstack = []
            for i in stack:
                newstack.append(i.right)
                newstack.append(i.left)
            stack = [i for i in newstack if i]
        return res