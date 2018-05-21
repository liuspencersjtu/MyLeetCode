# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inOrderTranversal(t):
            if t == None:
                return []
            return inOrderTranversal(t.left)+[t.val]+inOrderTranversal(t.right)
        res = inOrderTranversal(root)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True