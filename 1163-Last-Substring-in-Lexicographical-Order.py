class Solution:
    def lastSubstring(self, s: str) -> str:
        cur = s[0]
        for i in range(1,len(s)):
            if s[i]>cur[0]:
                cur = s[i]
            elif s[i]<cur[0]:
                cur+=s[i]
            else:#s[i]=cur[0]
                if cur+s[i:]>s[i:]:
                    cur+=s[i]
                else:
                    cur=s[i]
        return cur
