class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s):
            return s == s[::-1]
        def dfs(s, path, res):
            if not s:
                res.append(path)
            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]], res)
        dfs(s, [], res)
        return res
            
