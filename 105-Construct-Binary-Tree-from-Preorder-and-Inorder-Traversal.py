# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        val = preorder.pop(0)
        tree = TreeNode(val)
        i = inorder.index(val)
        tree.left = self.buildTree(preorder[:i],inorder[:i])
        tree.right = self.buildTree(preorder[i:],inorder[i+1:])
        return tree
        
        '''
        left = inorder[:i]
        right = inorder[i+1:]
        preleft = [i for i in preorder if i in left]
        preright = [i for i in preorder if i in right]
        '''
        '''
        preleft = []
        preright = []
        for item in preorder:
            if item in left:
                preleft.append(item)
            else:
                preright.append(item)
        '''
        '''
        tree.left = self.buildTree(preleft,left)
        tree.right = self.buildTree(preright,right)
        return tree
        '''


        '''
        hint: use dict(hash map) to accelerate

sample 60 ms submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        return root

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    # 12:00
    def buildTree(self, preorder, inorder):
        dicinorder = {}
        for i,val in enumerate(inorder):
            dicinorder[val] = i
        start, end = 0, len(inorder)
        return self.helper(start, end, preorder, dicinorder)
    
    def helper(self, start, end, preorder, dicinorder):
        if start == end:
            return None
        root = TreeNode(preorder.pop(0))
        inorderIndex = dicinorder[root.val]
        root.left = self.helper(start, inorderIndex, preorder, dicinorder)
        root.right = self.helper(inorderIndex+1, end, preorder, dicinorder)
        return root
'''