class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        maxDepth = 0
        tmp = 0
        for it in seq:
            if it == '(':
                tmp+=1
                maxDepth = max(maxDepth,tmp)
            else:
                tmp-=1
        target = maxDepth//2
        res = [0]*len(seq)
        tmp = 0
        for i in range(len(seq)):
            if seq[i]=='(':
                tmp+=1
            if tmp>target:
                res[i]=1
            if seq[i]==')':
                tmp-=1
        return res
