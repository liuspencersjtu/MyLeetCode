# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        from functools import lru_cache
        @lru_cache(2023)
        def helper(root):
            if not root:
                return 0
            option1 = helper(root.left) + helper(root.right)
            grandkids = []
            for node in [root.left, root.right]:
                if node:
                    grandkids.append(node.left)
                    grandkids.append(node.right)
            option2 = root.val
            for node in grandkids:
                option2 += helper(node)
            return max(option1, option2)
        return helper(root)
            
