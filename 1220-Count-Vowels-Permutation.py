class Solution:
    def countVowelPermutation(self, n: int) -> int:
        memo = {}
        def dp(n, c):
            if n==1:
                return 1
            elif (n,c) in memo:
                return memo[(n,c)]
            elif c == 'a':
                res = dp(n-1,'e') + dp(n-1,'i') + dp(n-1,'u')
            elif c == 'e':
                res = dp(n-1,'a') + dp(n-1,'i')
            elif c == 'i':
                res = dp(n-1,'e') + dp(n-1,'o')
            elif c == 'o':
                res = dp(n-1,'i')
            elif c == 'u':
                res = dp(n-1,'i') + dp(n-1,'o')
            memo[(n,c)]=res
            return res
        return (dp(n,'a')+dp(n,'e')+dp(n,'i')+dp(n,'o')+dp(n,'u'))%(10**9+7)
