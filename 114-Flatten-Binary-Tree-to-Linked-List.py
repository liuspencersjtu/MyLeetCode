# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        queue = []
        def preorder(root):
            if not root:
                return
            queue.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        queue = queue[::-1]
        head = TreeNode(-1)
        p = head
        while queue:
            p.right = queue.pop()
            p = p.right
            p.left = None
        # return head.right
            
        
