class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        from collections import defaultdict,Counter
        memo = defaultdict(int)
        cnt = Counter(t)
        t = set(t)
        i,j = 0, 0
        res = '#'*(m+1)
        def check():
            for s in t:
                if memo[s]<cnt[s]:
                    return False
            return True
        while j<m:
            while j<m and not check():
                memo[s[j]] += 1
                j += 1
            while i<=j and check():
                if len(res)>  j-i:
                    res = s[i:j]
                memo[s[i]] -= 1
                i += 1
        if len(res)>m:
            return ''
        return res
        
