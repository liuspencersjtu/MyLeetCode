# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 边界条件两个
        if not root:
            return []
        elif root.val == sum and not root.left and not root.right:
            return [[root.val]]
        return self.dfs(root, [], root.val, sum, [root.val])
    
    def is_valid(self, node):
        if node:
            return True
        else:
            return False
        
    def match(self, current, child, target):
        if not child.left and not child.right and current+child.val == target:
            return True
        else:
            return False
        
    def dfs(self, node, res, current, target, path):
        for n in [node.left, node.right]:
            if self.is_valid(n):
                if self.match(current, n, target):
                    res.append(path+[n.val])
                else:
                    self.dfs(n, res, current+n.val, target, path+[n.val])
        return res
        
