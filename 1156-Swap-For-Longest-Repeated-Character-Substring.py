import itertools
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        groups = [[k, len(list(t))] for k,t in itertools.groupby(text)]
        res = 0
        memo = collections.Counter(text)
        for k,l in groups:
            res = max(res, min(l+1,memo[k]))
        # try to replace things
        for i in range(1,len(groups)-1):
            if groups[i-1][0] == groups[i+1][0] and groups[i][1]==1:
                res = max(res, min(groups[i-1][1]+groups[i+1][1]+1, memo[groups[i-1][0]]))
        return res
            
