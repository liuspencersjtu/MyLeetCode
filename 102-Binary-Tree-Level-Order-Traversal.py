# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.queue = []
        self.answer = []
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #self.answer += [[root.val]
        self.queue += [root]
        while self.queue != []:
            thisLevel = []
            nextQueue = []
            for item in self.queue:
                
                if item == None:
                    pass
                else:
                    nextQueue += [item.left, item.right]
                    thisLevel += [item.val]
            if thisLevel != []:
                self.answer += [thisLevel]
            self.queue = nextQueue
            
        return self.answer