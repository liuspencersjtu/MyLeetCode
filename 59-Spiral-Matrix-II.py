class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def flip(A):
            return A[::-1]
        
        def diagonal(A):
            return list(zip(*A))
        
        res = []
        l = n * n + 1
        while l > 1:
            l, r = l - len(res), l
            res = [list(range(l, r))] + list(zip(*res[::-1]))
        return res
