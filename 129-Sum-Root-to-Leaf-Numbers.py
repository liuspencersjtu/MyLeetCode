# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # bfs
        res = 0
        stack = [root]
        while stack:
            next_stack = []
            for node in stack:
                if not node.left and not node.right:
                    res += node.val
                if node.left:
                    node.left.val = int(str(node.val)+str(node.left.val))
                    next_stack.append(node.left)
                if node.right:
                    node.right.val = int(str(node.val)+str(node.right.val))
                    next_stack.append(node.right)
            stack = next_stack
        return res
