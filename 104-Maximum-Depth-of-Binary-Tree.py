# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution： bfs
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]
        depth = 0
        while root and stack:
            depth += 1
            newstack = []
            for i in stack:
                newstack.append(i.left)
                newstack.append(i.right)
            stack = [i for i in newstack if i]
            
        return depth