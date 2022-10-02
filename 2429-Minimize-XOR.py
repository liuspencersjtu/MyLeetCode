class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def numOfBits(num):
            res = 0
            while num != 0:
                res += 1
                num &= num-1
            return res
        x1 = numOfBits(num1)
        x2 = numOfBits(num2)
        if x1>=x2:
            tmp = num1
            for i in range(x1-x2):
                tmp = tmp&(tmp-1)
            return tmp
        else:
            L = max(len(bin(num1)[2:]),len(bin(num2)[2:]))
            num3 = int('1'*L, base=2) ^ num1
            tmp = num3
            for i in range(x2-x1):
                tmp &= tmp-1
            return (num3 - tmp)|num1
        # # 1011010100
        # # 0100101011

