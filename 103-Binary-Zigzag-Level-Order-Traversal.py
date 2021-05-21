# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        zigzag = False
        while queue:
            r2 = []
            q2 = []
            for node in queue:
                r2.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if zigzag:
                res.append(r2[::-1])
            else:
                res.append(r2)
            queue = q2
            zigzag = not zigzag
        return res
