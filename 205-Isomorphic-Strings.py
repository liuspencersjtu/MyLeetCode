class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        memo1 = defaultdict(int)
        memo2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if memo1[s[i]] != memo2[t[i]]:
                return False
            memo1[s[i]] = memo2[t[i]] = i+1
        return True
       # 算是DP问题吧，简单来说，只要记录目前出现的字母之前最后一次出现的位置就好了，i+1是为了把0空出来作为默认值 
