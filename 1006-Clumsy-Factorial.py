class Solution:
    def clumsy(self, N: int) -> int:
        m = N//4
        k = N%4
        res = 0
        if m>=1:
            res = N*(N-1)//(N-2)+(N-3)
            for i in range(N-4,k,-4):
                res -= (i*(i-1))//(i-2)-(i-3)
        if k==0:
            pass
        elif k==1:
            res-=1
        elif k==2:
            res-=2*1
        else:#k==3
            res-=3*2/1
        if m==0:
            return int(-res)
        return int(res)
