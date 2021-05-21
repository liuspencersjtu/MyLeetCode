# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 1
        queue = [root]
        while queue:
            q1 = []
            for node in queue:
                if not node.left and not node.right:
                    return level
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            level += 1
            queue = q1
        return level
