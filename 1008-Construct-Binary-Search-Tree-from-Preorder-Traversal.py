# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        mid = -1
        for i in range(len(preorder)):
            if preorder[i]>val:
                mid=i
                break
        if mid==-1:
            root.left = self.bstFromPreorder(preorder)
            return root
        else:
            root.left = self.bstFromPreorder(preorder[0:mid])
            root.right = self.bstFromPreorder(preorder[mid:])
            return root
