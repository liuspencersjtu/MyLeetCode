class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = 0
        while m != n:
            m >>= 1
            n >>= 1
            diff += 1
        return m << diff
