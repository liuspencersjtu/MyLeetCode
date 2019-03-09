class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        for item in s.split():
            stack.insert(0,item)
        return ' '.join(stack)
