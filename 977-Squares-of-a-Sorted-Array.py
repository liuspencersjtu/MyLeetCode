class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        b=map(lambda x:x**2, A)
        b.sort()
        return b
