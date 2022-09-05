class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        from math import perm
        L = list(map(int, str(n+1)))
        res = sum([9*perm(9,i) for i in range(len(L)-1)])
        s = set()
        for i, it in enumerate(L):
            if i==0:
                for j in range(1, it):
                    if j not in s:
                        res += perm(10-len(s)-1, len(L)-i-1)
            else:
                for j in range(it):
                    if j not in s:
                        res += perm(10-len(s)-1, len(L)-i-1) #perm(0,0)==1
            if it in s:
                break
            s.add(it)
        return res
        
        # https://leetcode.com/problems/count-special-integers/discuss/2425271/JavaPython-Math
        # 1012. Numbers With Repeated Digits
        # from math import perm
        # N = n
        # L = list(map(int, str(N + 1)))
        # n = len(L)
        # res = sum(9 * perm(9, i) for i in range(n - 1))
        # s = set()
        # for i, x in enumerate(L):
        #     for y in range(i == 0, x):
        #         if y not in s:
        #             res += perm(9 - i, n - i - 1)
        #     if x in s: break# for case like 13367, when we finish 130xx 131xx 132xx we do not need to consider 133xx, since this prefix does not meet requirement
        #     s.add(x)
        # return res
