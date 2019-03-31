import math
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N==0:
            return "0"
        res = []
        while N:
            tmp = math.ceil(N/-2)
            res.insert(0,str(N-tmp*(-2)))
            N = tmp
        return ''.join(res)
