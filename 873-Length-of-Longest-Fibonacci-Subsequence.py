class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Thanks to [https://buptwc.github.io/2018/07/22/Leetcode-873-Length-of-Longest-Fibonacci-Subsequence/]
        dp = collections.defaultdict(int)
        s = set(A)
        res = 0
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
                    res = max(res, dp[A[i], A[j]])
        return res