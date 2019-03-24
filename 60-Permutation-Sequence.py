#from functools import lru_cache
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #@lru_cache()
        def help(n):
            total = 1
            for i in range(1,n+1):
                total *=i
            return total
        res = []
        lst = list(range(1,n+1))
        memo = []
        k-=1
        for i in range(n-1,0,-1):
            ##
            a = k//help(i)
            memo.append(a)
            res.append(lst.pop(a))
            k = k%help(i)
        res.append(lst[0])
        print(memo, lst)
        res = map(str, res)
        return ''.join(res)
