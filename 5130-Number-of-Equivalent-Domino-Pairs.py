import collections
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        memo = collections.defaultdict(int)
        for a,b in dominoes:
            if a>b:
                memo[(b,a)]+=1
            else:
                memo[(a,b)]+=1
        res = 0
        for i in memo:
            res += memo[i]*(memo[i]-1)//2
        return res
        
