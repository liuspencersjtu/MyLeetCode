class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(S, pattern):
            a = ord('a')
            z = ord('z')
            N = len(S)
            M = len(pattern)
            i,j = 0, 0
            while i<N:
                if j>=M:
                    if 'a'<=S[i]<='z':
                        i += 1
                    else:
                        return False
                else:
                    if S[i] == pattern[j]:
                        i += 1
                        j += 1
                    else:
                        if 'a'<=S[i]<='z':
                            i += 1
                        else:
                            return False
            if j>=M:
                return True
            else:
                return False
        res = []
        for it in queries:
            res.append(match(it,pattern))
        return res
