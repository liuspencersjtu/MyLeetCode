class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # 可以计算最长‘前缀’回文字符串
        # 可以用马拉车，但是在面试中现场写马拉车的出错概率还是比较高的
        reversed_s = s[::-1]
        N = len(s)
        for i in range(len(s)):
            if s[:N-i] == reversed_s[i:]:
                return reversed_s[:i] + s
        return s
        # 这样时间复杂度为O(N^2),空间复杂度为O(N)
