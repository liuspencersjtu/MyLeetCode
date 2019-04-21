class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        #search space = [L,] 
        previousmaxL = []
        curr = 0
        if L>1:
            previousmaxL += [0]*(L-1)
        for i in range(L,N+1):
            #
            curr = max(curr, sum(A[i-L:i]))
            previousmaxL.append(curr)
        
        previousmaxM = []
        curr = 0
        if M>1:
            previousmaxM += [0]*(M-1)
        for i in range(M,N+1):
            #
            curr = max(curr, sum(A[i-M:i]))
            previousmaxM.append(curr)
        #print(previousmaxL)
        #print(previousmaxM)
        
        afterL = []
        curr = 0
        if L>1:
            afterL += [0]*(L-1)
        for i in range(N-L-1,-2,-1):
            curr = max(curr, sum(A[i+1:i+L+1]))
            afterL.append(curr)
        afterL = afterL[::-1]
        
        afterM = []
        curr = 0
        if M>1:
            afterM += [0]*(M-1)
        for i in range(N-M-1,-2,-1):
            curr = max(curr, sum(A[i+1:i+M+1]))
            afterM.append(curr)
        afterM = afterM[::-1]
        #print(afterL)
        #print(afterM)
        
        res = 0
        for i in range(N-1):
            res = max(previousmaxL[i]+afterM[i+1],res)
            res = max(previousmaxM[i]+afterL[i+1],res)
        return res
