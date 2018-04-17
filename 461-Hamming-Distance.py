class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        result = 0
        while z>0:
            result += (z%2)
            z = z//2
        return result
            