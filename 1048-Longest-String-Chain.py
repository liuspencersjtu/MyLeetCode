import functools
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = [set()]*17
        for it in words:
            memo[len(it)].add(it)
        @functools.lru_cache()
        def dp(word):
            ret = 1
            n = len(word)
            for i in range(n):
                if word[:i]+word[i+1:] in memo[n-1]:
                    ret = max(ret, dp(word[:i]+word[i+1:])+1)
            return ret
        res = 0
        for word in words:
            res = max(res, dp(word))
        return res
            
