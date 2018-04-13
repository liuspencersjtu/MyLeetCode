# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
            newTree = TreeNode(root.val)
            newTree.right = self.invertTree(root.left)
            newTree.left = self.invertTree(root.right)
            return newTree
            