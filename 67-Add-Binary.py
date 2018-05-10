class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def toDecimal(num):
            res = 0
            level = 0
            while num:
                res += (num%10)*(2)**level
                level += 1
                num = num//10
            return res
        def toBinary(num):
            res = 0
            level = 0
            while num:
                res += (num%2)*(10)**level
                level += 1
                num = num//2
            return res
        a = toDecimal(int(a))
        b = toDecimal(int(b))
        return str(toBinary(a+b))