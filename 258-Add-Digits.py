class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            s = str(num)
            num = sum(map(int, s))
        return num