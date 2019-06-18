class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        memo = collections.defaultdict(int)
        res = []
        tmp = list(zip(values,labels))
        tmp.sort()
        while num_wanted>0 and tmp != []:
            v, l = tmp.pop()
            if memo[l]<use_limit:
                res.append(v)
                memo[l]+=1
                num_wanted -= 1
        return sum(res)
            
            
