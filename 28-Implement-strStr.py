class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L = len(needle)
        for i in range(len(haystack)-L+1):
            if haystack[i:i+L] == needle:
                return i
        return -1
