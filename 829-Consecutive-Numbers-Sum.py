class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = 1
        res = 1
        while (n+1)*(n+2)<=2*N:
            if (2*N)%(n+1) != 0:
                n += 1
            else:
                if ((2*N)/(n+1)-n)%2 == 0:
                    res += 1
                n += 1
        return res
            