class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        memo = {}
        for i in s:
            if memo.get(i,0) == 0:
                memo[i] = 1
            else:
                memo[i] += 1
                    
        for i in t:
            if memo.get(i,0) == 0:
                return i
            else:
                memo[i] -= 1