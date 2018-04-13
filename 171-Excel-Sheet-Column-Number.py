class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        base = ord('A') -1
        rnd = 0
        for item in s[::-1]:
            value += (ord(item) - base) * 26**rnd
            rnd += 1
        return value