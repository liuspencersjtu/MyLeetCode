# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # recursive traversal too slow
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes(self, root: TreeNode) -> int:
        # time: o(lg n * lg n) 时间分析是重点
        if not root:
            return 0
        p, q  = root, root
        lmh, rmh = 0, 0#left most height and right most height
        while p:
            lmh += 1
            p = p.left
        while q:
            rmh += 1
            q = q.right
        if lmh == rmh:
            return 2**lmh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
