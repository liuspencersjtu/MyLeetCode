# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:
                return [None]
            else:
                return [root.val] + helper(root.left) + helper(root.right)
        return str(helper(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        t = TreeNode(None)
        def helper(data,t1):
            if not data:
                return
            a = data.pop(0)
            if a == None:
                t1 = None
                return t1
            else:
                t1 = TreeNode(a)
                #t1.left = TreeNode(None)
                #t1.right = TreeNode(None)
                t1.left = helper(data,t1.left)
                t1.right = helper(data,t1.right)
                return t1
        t = helper(data,t)
        return t
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))