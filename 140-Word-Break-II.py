class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # dfs
        if not s:
            return []
        res = []
        wordSet = set(wordDict)
        def dfs(s, path, res):
            if not s:
                res.append(' '.join(path))
            for i in range(1, len(s)+1):#这里的边界要小心
                if s[:i] in wordSet:
                    dfs(s[i:], path+[s[:i]], res)
        dfs(s, [], res)
        return res
