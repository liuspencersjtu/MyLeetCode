class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return ""
        jumpover = 0
        res = []
        stack = []
        for it in S[1:]:
            if it == "(":
                if jumpover:
                    jumpover = 0
                else:
                    stack.append(it)
                    res.append(it)
            elif it == ")":
                if stack:
                    stack.pop()
                    res.append(it)
                else:
                    jumpover = 1
        return ''.join(res)
