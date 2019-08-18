# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res = []
        queue = [root]
        while queue:
            newqueue = []
            cur = 0
            for it in queue:
                cur += it.val
                if it.left:
                    newqueue.append(it.left)
                if it.right:
                    newqueue.append(it.right)
            res.append(cur)
            queue = newqueue
        tmp = [(v, k+1) for k,v in enumerate(res)]
        return sorted(tmp,reverse=True)[0][1]
