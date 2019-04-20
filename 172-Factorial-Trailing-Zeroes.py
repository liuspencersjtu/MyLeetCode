class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 0
        while 5**i<=n:
            i+=1
        res = 0
        for j in range(1,i):
            res += n//(5**j)
        return res
