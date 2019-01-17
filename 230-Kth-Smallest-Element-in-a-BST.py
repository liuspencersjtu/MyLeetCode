# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        n=0
        def helper(root):
            nonlocal n
            #if n == k:
            #    return root
            if not root:
                #是none
                return
            else:
                #先左
                helper(root.left)
                n+=1
                print(n,k,root.val)
                if n==k:
                    self.res = root.val
                    return root.val
                helper(root.right)
                '''
                if not p:
                    #如果左边是空
                    #再中（自己）
                    n+=1
                    #最后右边
                    helper(root.right)
                else:
                    #左边不是空
                ''' 
                #return q
        helper(root)
        return self.res
