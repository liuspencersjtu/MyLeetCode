class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(2**n):
            res.append(i^(i>>1))
        return res
