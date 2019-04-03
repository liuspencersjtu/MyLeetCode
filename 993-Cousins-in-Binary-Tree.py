# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [root]
        while queue:
            newqueue = []
            ##
            cnt = 0
            for it in queue:
                tmp = 0
                if it.left and it.left.val in (x,y):
                    tmp = 1
                if it.right and it.right.val in (x,y):
                    tmp = 1
                cnt+=tmp
                if it.left:
                    newqueue.append(it.left)
                if it.right:
                    newqueue.append(it.right)
            if cnt == 2:
                return True
            queue = newqueue
        return False
