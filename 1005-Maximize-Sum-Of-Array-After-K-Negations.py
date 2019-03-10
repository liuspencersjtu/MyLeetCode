class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        pos, neg = [], []
        for i in A:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        pos.sort()
        neg.sort()
        #print(pos,neg)
        m,n = len(neg), len(pos)
        if K<=m:
            res = sum(pos)
            while neg:
                if K>0:
                    res+=-neg.pop(0)
                    K-=1
                else:
                    res+=neg.pop(0)
            return res
        else:
            A = [-i for i in neg]+pos
            A.sort()
            #print(A)
            return sum(A[1:])+A[0]*(-1)**((K-m)%2)
