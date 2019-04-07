# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root,cur_sum):
            if not root.left and not root.right:
                self.res += cur_sum*2+root.val
            else:
                for it in (root.left, root.right):
                    if it:
                        dfs(it, cur_sum*2+root.val)
        dfs(root,0)
        return self.res%(10**9+7)
