# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        head = TreeNode(10000)
        head.left = root
        to_delete = set(to_delete)
        def dfs(root,parent,idx):
            if not root:
                return
            dfs(root.left,root,0)
            dfs(root.right,root,1)
            if root.val in to_delete:
                #print(root.val)
                res.append(root.left)
                res.append(root.right)
                if idx==0:
                    parent.left=None
                elif idx==1:
                    parent.right=None
        dfs(root,head,0)
        if head.left:
            res.append(head.left)
        res = [it for it in res if it]
        return res
                
