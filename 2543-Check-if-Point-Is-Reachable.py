class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        from math import gcd
        a = gcd(targetX, targetY)
        return a&(a-1)==0
