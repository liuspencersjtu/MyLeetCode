# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 看到tree的题上来直接写helper果然是没错的。。。
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.xleft,self.xright = 0,0
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == x:
                self.xleft = left
                self.xright = right
            return left+right+1
        N = dfs(root)
        if max(self.xleft,self.xright,N-self.xleft-self.xright-1)>N//2:
            return True
        return False
