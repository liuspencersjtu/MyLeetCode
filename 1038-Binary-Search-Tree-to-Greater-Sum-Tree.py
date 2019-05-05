# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(root, val):
            if root==None:
                return val
            tmp = inorder(root.right, val)
            root.val = root.val + tmp
            tmp2 = inorder(root.left, root.val)
            return tmp2
        inorder(root, 0)
        return root
