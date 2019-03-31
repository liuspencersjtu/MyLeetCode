class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        B = [str(it) for it in A]
        a = int(''.join(B),2)
        res = []
        while a:
            if a%5==0:
                res.insert(0,True)
            else:
                res.insert(0,False)
            a = a//2
        if len(res)<len(A):
            res = [True]*(len(A)-len(res))+res
        return res
