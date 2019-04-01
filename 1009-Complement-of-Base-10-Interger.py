class Solution:
    def bitwiseComplement(self, N: int) -> int:
        a = bin(N)[2:]
        res = 0
        cur = 1
        for it in a[::-1]:
            if it == '0':
                #
                res += cur
            cur*=2
        return res
