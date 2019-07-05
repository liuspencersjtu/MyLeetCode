# question: https://www.1point3acres.com/bbs/thread-531999-1-1.html

# 题目大概是这样的：
# 给你一个由'.'和'S'组成的长度为N的数组A，你可以最多做K次操作，每次操作选择一个数组中的位置，把相应位置连同左右邻居都变成'.'。
# 问K次操作之后，数组中最多可以有多少个'.'。
# 输入：
# N K
# A
# 输出
# 数组A中'.'的个数。

# Constraint
# 1 <= N <= 1000
# 1 <= K <= 1000

# 然后我贴几个测试数据
# 格式：
# N K
# A
# Answer

# 67 4
# SS.S...S....SS..S..S.S.S...SS...SSS..SS.SS.SSSSS...S.S.S...S......S
# 48

# 29 2
# .S.....SSSSS.SSSS...SS.SSS.SS
# 18

# 79 6
# .S...SSS.SSS..SSSS.SSSSS.SS.S.SS.SS.SSSSSSS.SS...SS.S.SSS.SS.S.SS..S..S.SSS.SS.
# 47

# 276 23
# SSSSSS.SSS..SSS.SS.S.SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS.SS.SSSSSSSSSSSSSSSSSSS.SSSSSS.SSSSSSSSSSSSSSSSSS.SSSSSSSSSSSSSSSSSSSSSSSSS.SSSSSSSSSSSSSSSSS.SSSSSSSSSSSSSS.S.SSS.SSSSSS.SSSSSSSSSSS.SSSSSSSSSSSSS.SSSSSSS.S.SSSS.SSSSSSSSSSSS.SSSSSSSSSSSSSSSS.SSS.S.SS.SSSSSSS.SSSSSSSS.SSS.S.
# 100


from functools import lru_cache
def solution(A,K):
    N = len(A)
    @lru_cache(512)
    def dp(n,k):
        if n<=0:
            return 0
        elif n<=3:
            if k>0:
                return n
            else:
                return len(list(filter(lambda x: x=='.', A[:n])))
        if k == 0:
            return len(list(filter(lambda x: x=='.', A[:n])))
        a = dp(n-3,k) + len(list(filter(lambda x: x=='.', A[n-3:n])))
        b = dp(n-3,k-1) + 3
        c = dp(n-2,k-1) + 2
        d = dp(n-1,k-1) + 1
        e = dp(n-1,k) + len(list(filter(lambda x: x=='.', A[n-1:n])))
        f = dp(n-2,k) + len(list(filter(lambda x: x=='.', A[n-2:n])))
        return max(a,b,c,d,e,f)
    return dp(N,K)
