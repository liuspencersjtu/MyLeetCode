import functools
# remember using lru_cache to store the intermediate result
# it's a DP problem, not just recursive
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        if not wordDict:
            return s==''
        k = max(len(it) for it in wordDict)
        #wordDict.sort(reverse=True)
        @functools.lru_cache()
        def helper(s):
            if s=='':
                return True
            res = False
            for i in range(k,-1,-1):
                if s[:i] in wordDict:
                    if helper(s[i:]):
                        return True
            '''
            for it in wordDict:
                a = len(it)
                if it == s[:a]:
                    if helper(s[a:]):
                        return True
            '''
            return res
        return helper(s)
