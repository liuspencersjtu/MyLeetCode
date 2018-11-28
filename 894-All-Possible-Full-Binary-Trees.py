# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N==1:
            return [TreeNode(0)]
        #if N==2:
        #    return []
        if N%2==0:
            return []
        res = []
        # a interesting fact is if you write
        # t=TreeNode(0)
        # here, the answer will be wrong!
        for i in range(1,N-1):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-1-i)
            for node1 in left:
                for node2 in right:
                    t=TreeNode(0)
                    t.left = node1
                    t.right = node2
                    res.append(t)
        return res