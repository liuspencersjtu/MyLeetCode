class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        res = 0
        for it in s:
            if it=='(':
                stack += 1
                res = max(stack, res)
            elif it==')':
                stack -= 1
        return res
