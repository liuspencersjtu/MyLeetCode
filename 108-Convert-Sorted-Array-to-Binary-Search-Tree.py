# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return 
        N = len(nums)
        root = TreeNode(nums[N//2])
        root.left = self.sortedArrayToBST(nums[:N//2])
        root.right = self.sortedArrayToBST(nums[N//2+1:])
        return root
