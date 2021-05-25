class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [c.lower() for c in s if 'a'<=c<='z' or 'A'<=c<='Z' or '0'<=c<='9']
        s = ''.join(ss)
        return s == s[::-1]
