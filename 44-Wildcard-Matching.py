class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # nice dp question. check whether the top i char of p can match top j char of s
        t = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
        t[0][0] = True
        for i in range(1, len(p) + 1):
            t[i][0] = t[i-1][0] and p[i-1] == '*'
        for i in range(1, len(p) + 1):
            for j in range(1, len(s)+1):
                if p[i-1] != '*':
                    t[i][j] = (p[i-1] == s[j-1] or p[i-1] == '?') and t[i-1][j-1]
                else:
                    t[i][j] = t[i][j-1] or t[i-1][j]
        return t[-1][-1]
