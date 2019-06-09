# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(root, val):
            if not root:
                return False
            cur = val+root.val
            if not root.left and not root.right:
                if cur<limit:
                    return False
                else:
                    return True
            res1, res2 = dfs(root.left,cur), dfs(root.right,cur)
            if not res1:
                root.left = None
            if not res2:
                root.right = None
            if not res1 and not res2:# and cur<limit:
                return False
            else:
                return True
        newroot = TreeNode(0)
        newroot.left = root
        dfs(newroot,0)
        return newroot.left
