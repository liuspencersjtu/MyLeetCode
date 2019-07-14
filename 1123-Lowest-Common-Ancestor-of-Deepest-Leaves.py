# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def bfs(root):
            # find deepest leaves
            queue = [root]
            while queue!=[]:
                newqueue = []
                for it in queue:
                    if it.left != None:
                        newqueue.append(it.left)
                    if it.right != None:
                        newqueue.append(it.right)
                if newqueue == []:
                    return queue
                queue = newqueue
        self.leaves = set([it.val for it in bfs(root)]) 
        self.N = len(self.leaves)
        # print(self.leaves,self.N)
        def dfs(root):
            if root == None:
                return
            if root.left == None and root.right == None:
                if root.val in self.leaves:
                    root.reached = [root.val]
                    if len(root.reached) == self.N:
                        return root
                else:
                    root.reached = []
                return
            a = dfs(root.left)
            b = dfs(root.right)
            if a:
                return a
            if b:
                return b
            if root.val in self.leaves:
                root.reached = [root.val]
            else:
                root.reached = []
            if root.left:
                root.reached += root.left.reached
            if root.right:
                root.reached += root.right.reached
            # print(root.val, root.reached)
            if len(root.reached) == self.N:
                return root
            return
        return dfs(root)
