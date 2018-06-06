class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def backspace(s):
            stack = []
            for i in range(len(s)):
                a = s[i]
                if a == '#' and stack != []:
                    stack.pop()
                else:
                    stack.append(a)
        return backspace(S) == backspace(T)