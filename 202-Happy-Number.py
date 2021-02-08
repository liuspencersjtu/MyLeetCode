class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquare(n):
            res = 0
            while n!=0:
                res += (n%10)**2
                n = n//10
            return res
        lookup = set()
        while n!=1 and n not in lookup:
            lookup.add(n)
            n = getSquare(n)
        return True if n==1 else False
