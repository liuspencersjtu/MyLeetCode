# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            newstack = []
            def f(x,y):
                x.next = y
            for i in range(1,len(stack)):
                stack[i-1].next = stack[i]
            stack[-1].next = None
            for i in stack:
                newstack.append(i.left)
                newstack.append(i.right)
            stack = [i for i in newstack if i]