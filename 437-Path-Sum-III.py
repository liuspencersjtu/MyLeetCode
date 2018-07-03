# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, psum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        num = root.val
        if num == psum:
            return 1
        return self.pathSum(root.left, psum) + self.pathSum(root.right, psum) + self.pathSum(root.left, psum - num) +self.pathSum(root.right, psum - num)