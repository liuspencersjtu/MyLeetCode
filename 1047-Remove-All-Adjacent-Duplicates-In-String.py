class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for it in S:
            if stack and stack[-1]==it:
                stack.pop()
            else:
                stack.append(it)
        return ''.join(stack)
