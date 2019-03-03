from collections import defaultdict
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        N = len(A)
        memo = defaultdict(int)
        cnt = defaultdict(int)
        for item in A:
            temp = defaultdict(int)
            for i in item:
                temp[i]+=1
            for key in temp:
                memo[key]+=1
                cnt[key] = min(cnt[key], temp[key]) if cnt[key]!=0 else temp[key]
        res = []
        for item in memo:
            if memo[item]>=N:
                for _ in range(cnt[item]):
                    res.append(item)
            
        return res
        
