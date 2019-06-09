class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {}
        for i,c in enumerate(text):
            last[c]=i
        res = ''
        left = 0
        while last:
            right = min(last.values())
            c, i = min((text[k],k) for k in range(left,right+1) if text[k] not in res)
            res += c
            left = i+1
            last.pop(c)
        return res
