class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S=="":
            return [""]
        res = []
        n = '0123456789'
        for i in range(len(S)):
            if S[i] in n:
                continue
            else:
                p = S[:i]+S[i].lower()
                q = S[:i]+S[i].upper()
                for item in self.letterCasePermutation(S[i+1:]):
                    res.append(p+item)
                    res.append(q+item)
                break
        if S not in res:
            res.append(S)
        return list(res)
        
