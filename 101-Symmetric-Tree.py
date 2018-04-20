# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        stack = [root.left,root.right]
        res = True
        while [i for i in stack if i]:
            next_level = []
            for i in stack:
                if i:
                    next_level.append(i.left)
                    next_level.append(i.right)
            while stack:
                a=stack.pop(0)
                b=stack.pop()
                if not a and b:
                    return False
                elif not b and a:
                    return False
                elif not a and not b:
                    pass
                elif not(a.val == b.val):
                    return False
            stack = next_level
            
                
        return True