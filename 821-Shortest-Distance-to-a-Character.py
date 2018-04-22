class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        S=list(S)
        res = []
        l = len(S)
        for i in range(l):
            if S[i] == C:
                res += [0]
            else:
                k1 = 0
                k2 = 0
                while i-k1>=0:
                    if S[i-k1] == C:
                        break
                    elif i-k1 == 0:
                        k1 = 99999
                    k1 += 1
                while i+k2<=l-1:
                    if S[i+k2] == C:
                        break
                    elif i+k2 == l-1:
                        k2 = 99999
                    k2 += 1
                res += [min(k1,k2)]
        return res