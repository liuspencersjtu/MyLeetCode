# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        if not voyage:
            return [-1]
        a = voyage.pop(0)
        if a!=root.val:
            return [-1]
        if root.left:
            if root.right:
                if (root.left and root.left.val not in voyage) or (root.right and root.right.val not in voyage):
                    return [-1]
                else:
                    m, n = voyage.index(root.left.val), voyage.index(root.right.val)
                    if m==0:
                        res1=self.flipMatchVoyage(root.left, voyage[:n])
                        res2=self.flipMatchVoyage(root.right, voyage[n:])
                    else:
                        res.append(root.val)
                        res1=self.flipMatchVoyage(root.left, voyage[m:])
                        res2=self.flipMatchVoyage(root.right, voyage[:m])
                    if -1 in res1 or -1 in res2:
                        return [-1]
                    else:
                        return res+res1+res2
            else:
                return self.flipMatchVoyage(root.left,voyage)
        else:
            if root.right:
                return self.flipMatchVoyage(root.right,voyage)
            else:
                if not voyage:
                    return []
                else:
                    return [-1]
