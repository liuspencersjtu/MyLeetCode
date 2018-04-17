class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (t1 == None) and (t2 == None):
            return None
        elif t2 == None:
            newtree = TreeNode(t1.val)
            newtree.left = self.mergeTrees(t1.left,None)
            newtree.right = self.mergeTrees(t1.right,None)
            return newtree
        elif t1 == None:
            newtree = TreeNode(t2.val)
            newtree.left = self.mergeTrees(None,t2.left)
            newtree.right = self.mergeTrees(None,t2.right)
            return newtree
        else:
            newtree = TreeNode(t1.val + t2.val)
            newtree.left = self.mergeTrees(t1.left,t2.left)
            newtree.right = self.mergeTrees(t1.right,t2.right)
            return newtree
        
    '''
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans
    '''
    '''
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        else:
            t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    '''