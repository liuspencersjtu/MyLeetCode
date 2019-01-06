class Solution:
    import math
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        if bound<2:
            return []
        i = math.floor(math.log(bound-1,x)) if x!=1 else 0
        for m in range(i+1):
            j = math.floor(math.log(bound-x**m,y)) if y!=1 else 0
            for n in range(j+1):
                res.append(x**m+y**n)
        return list(set(res))
