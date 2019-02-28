class Solution:
    def customSortString(self, S: str, T: str) -> str:
        from collections import defaultdict
        memo = defaultdict(int)
        for i in S:
            memo[i] = 0
        ans = ''
        for i in T:
            if i in memo:
                memo[i]+=1
            else:
                ans+=i
        for i in S:
            ans+=i*memo[i]
        return ans
