class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        def dfs(s, digits):
            if len(digits)==0:
                if s != '':
                    res.append(s)
            else:
                for c in phone[digits[0]]:
                    dfs(s+c,digits[1:])
        dfs('', digits)
        
        return res
