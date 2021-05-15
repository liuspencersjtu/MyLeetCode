# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # res = []
        from copy import deepcopy
        from functools import lru_cache
        @lru_cache(256)
        def helper(nodes):  
            if len(nodes) == 0:
                return [None]
            elif len(nodes) == 1:
                return [TreeNode(nodes[0])]
            res = []
            for i, node in enumerate(nodes):
                t = TreeNode(node)
                lefts = helper(nodes[:i])
                rights = helper(nodes[i+1:])
                for m in range(len(lefts)):
                    for n in range(len(rights)):
                        t.left = lefts[m]
                        t.right = rights[n]
                        res.append(deepcopy(t))
            return res
        return helper(tuple(range(1, n+1)))
