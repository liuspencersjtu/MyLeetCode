# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        '''
        if inorder == None or inorder == []:
            return None
        #if len(inorder) == 1:
        #    return TreeNode(inorder[0])
        
        val = postorder.pop()
        tree = TreeNode(val)
        i = 0
        #linorder = []
        #lpostorder = []
        while inorder[i] != val:
            #linorder.append(inorder.pop(0))
            #lpostorder.append(postorder.pop(0))
            i+=1
        inorder.pop(i)
        tree.left = self.buildTree(inorder[:i],postorder[:i])
        tree.right = self.buildTree(inorder[i:],postorder[i:])
        return tree
        '''
        if not inorder:
            return None
        val = postorder.pop(-1)
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:])
        return root
        