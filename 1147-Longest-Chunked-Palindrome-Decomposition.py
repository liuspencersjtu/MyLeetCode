class Solution:
    def longestDecomposition(self, text: str) -> int:
        if not text:
            return 0
        N = len(text)
        if N == 1:
            return 1
        length = 0
        for i in range(N-1,N//2-1,-1):
            length+=1
            if text[:length] == text[i:]:
                # print(text[:length],text[length:i])
                return 2 + self.longestDecomposition(text[length:i])
        return 1
