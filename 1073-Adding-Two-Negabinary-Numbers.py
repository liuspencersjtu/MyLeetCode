import math
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def getvalue(arr):
            res = 0
            i = 0
            while arr:
                res+=(-2)**i*arr.pop()
                i+=1
            return res
        a, b = getvalue(arr1),getvalue(arr2)
        c = a+b
        def baseN2(num):
            res = []
            while num:
                #tmp = int(math.ceil(num/(-2)))
                #remain = num-tmp*(-2)
                #num = tmp
                remain = abs(num)%2
                num = (num-remain)//(-2)
                res.append(remain)
            if not res:
                return [0]
            return res[::-1]
        return baseN2(c)
