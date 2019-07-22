class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # https://buptwc.com/2018/06/26/Leetcode-858-Mirror-Reflection/
        k = 1
        while k*q %p != 0:
            k+=1
        if k%2 == 0:
            return 2
        else:
            r = k*q//p
            if r%2==0:
                return 0
            else:
                return 1
