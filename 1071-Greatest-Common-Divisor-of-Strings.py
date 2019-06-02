class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N = len(str1)
        div1 = set()
        for i in range(1,N+1):
            if N%i==0:
                k = N//i
                if str1 == str1[:i]*k:
                    div1.add(str1[:i])
        M = len(str2)
        div2 = set()
        for i in range(1,M+1):
            if M%i==0:
                k = M//i
                if str2 == str2[:i]*k:
                    div2.add(str2[:i])
        div3 = div1&div2            
        if len(div3)!=0:
            return max(div3)
        else:
            return ""
