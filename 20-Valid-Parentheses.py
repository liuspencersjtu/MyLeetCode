class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in ']})':
                if not stack:
                    return False
                p = stack.pop()
                if p!=memo[i]:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
