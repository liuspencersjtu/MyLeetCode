class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        s.sort()
        t=list(t)
        t.sort()
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
            return True