# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        if root == None:
            return []
        else:
            if not root.left and not root.right:
                return [root.val]
            else:
                return self.dfs(root.left) + self.dfs(root.right)
            
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        a = self.dfs(root1)
        b = self.dfs(root2)
        print(a)
        print(b)
        return a == b