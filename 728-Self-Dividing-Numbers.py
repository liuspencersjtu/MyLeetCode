class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def helper(num):
            num = str(num)
            digits = [int(i) for i in num]
            num = int(num)
            for digit in digits:
                if not digit or num%digit != 0:
                    return []
            return [num]
        res = []
        for num in range(left,right+1):
            res=res+helper(num)
        return res