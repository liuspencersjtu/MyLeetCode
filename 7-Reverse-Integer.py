class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=abs(x)
        res = 0
        while a:
            m = a%10
            a = a//10
            res = res*10+m
        if x>=0:
            if res<=2**31-1:
                return res
            else:
                return 0
        else:
            if -res>=-2**31:
                return -res
            else:
                return 0
