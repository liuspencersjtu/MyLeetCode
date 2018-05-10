class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n <0:
            return self.myPow(1/x,-n)
        if n == 0:
            return 1
        # n>0
        if n%2 == 0:
            return self.myPow(x,n/2)**2
        else:
            return (self.myPow(x,n//2)**2)*x
        # tips： binary search