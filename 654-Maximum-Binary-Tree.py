class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        m = nums.index(max(nums))
        res = TreeNode(nums[m])
        res.left = self.constructMaximumBinaryTree(nums[:m])
        res.right = self.constructMaximumBinaryTree(nums[m+1:])
        return res