class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        ## abcde
        ## a c e
        ## 11223
        ## 01122
        ## a e c
        ## 11112
        ## 22233
        prefix = []
        j = 0
        for i in range(len(s)):
            if j<len(t) and s[i]==t[j]:
                j += 1
            prefix.append(j)
        suffix = []
        j = len(t)
        for i in range(len(s)-1,-1,-1):
            if j>0 and s[i]==t[j-1]:
                j -= 1
            suffix.append(j)
        suffix = suffix[::-1]
        res = len(t)
        for i in range(len(s)-1):
            res = min(res, max(0,suffix[i+1]-prefix[i]))
        res = min(res, max(0,len(t)-prefix[len(s)-1]))
        res = min(res, max(0,suffix[0]))
        return res

