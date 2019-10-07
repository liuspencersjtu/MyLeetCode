class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        while s and s[-1] == '':
            s.pop()
        if s:
            return len(s[-1])
        else:
            return 0
