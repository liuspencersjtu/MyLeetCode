# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        temp = [root]
        while temp:
            nextTemp = []
            thisLevel = []
            for item in temp:
                if item:
                    thisLevel.append(item.val)
                    nextTemp.append(item.left)
                    nextTemp.append(item.right)
            if thisLevel:
                ans.insert(0,thisLevel)
            temp = nextTemp
        return ans
        