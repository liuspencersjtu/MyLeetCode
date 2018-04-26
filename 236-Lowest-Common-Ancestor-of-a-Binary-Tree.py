# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        self.ptag = False 
        self.qtag = False
        self.p = p.val
        self.q = q.val
        self.lca = []
        self.postorderTraversal(root)
        #if self.lca == []:
        #    return root
        #else:
        return self.lca[0]
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return 
        elif root.left == None and root.right == None:
            if root.val == self.p:
                self.ptag = True
            elif root.val == self.q:
                self.qtag = True
        else:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            #[root.val]
            if root.val == self.p:
                self.ptag = True
            elif root.val == self.q:
                self.qtag = True
            if self.ptag == True and self.qtag == True:
                self.lca += [root]
        '''
        if root is None:
            return root
    
        if root == p or root == q:
            return root
    
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
    
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right