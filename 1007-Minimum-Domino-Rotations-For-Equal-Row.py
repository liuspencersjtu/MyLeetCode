from collections import defaultdict
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        memo = defaultdict(set)
        memo1= defaultdict(int)
        memo2= defaultdict(int)
        k = 0
        for i,j in zip(A,B):
            memo[i].add(k)
            memo[j].add(k)
            memo1[i]+=1
            memo2[j]+=1
            k+=1
        key = -1
        for i in memo:
            if len(memo[i])==N:
                key=i
                break
        if key==-1:
            return -1
        else:
            return min(memo1[key],N-memo1[key],memo2[key],N-memo2[key])
            
