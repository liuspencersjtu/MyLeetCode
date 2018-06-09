class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        base = 1
        while base <= n:
            if base == n:
                return True
            else:
                base = base*3
        return False