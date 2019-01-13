class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # prefix sum的题目，用P[j]-P[i]表示第i-j个数之和,这里我们还要存放的是P[i]%K
        # 第一个P[0]作为anchor，当什么都没有放的时候，值为0
        P=[0]
        a=0
        for i in range(len(A)):
            a+=A[i]
            P.append(a%K)
        count = collections.Counter(P)
        res = 0
        for i in count.values():
            res+=i*(i-1)//2
        return res
