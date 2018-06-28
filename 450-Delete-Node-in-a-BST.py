# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findmax(self, root):
        if not root.right:
            return root
        else:
            return self.findmax(root.right)
        
    def deletemax(self, root):
        if not root.right:
            return None
        else:
            root.right = self.deletemax(root.right)
            return root
        
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                root = None
                return root
            elif not root.left:
                root = root.right
                return root
            else:
                r = self.findmax(root.left)
                root.val = r.val
                #r = None
                root.left = self.deletemax(root.left)
                return root
        # if still need searching
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
            
        return root