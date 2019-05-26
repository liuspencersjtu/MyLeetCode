class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if not A:
            return A
        i = len(A)-1
        temp = float('inf')
        while i>=0:
            #
            if A[i]>temp:
                break
            temp = A[i]
            i-=1
        if i == -1:
            return A
        # else i!=-1
        high = A[i]
        j=i+1
        N = len(A)
        while j<N and A[j]<high:
            j+=1
        A[i], A[j-1] = A[j-1], A[i]
        return A
