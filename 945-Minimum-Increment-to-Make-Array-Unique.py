class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        if not A:
            return 0
        tempMax = A[0]-1
        res = 0
        for i in range(len(A)):
            if A[i]<=tempMax:
                res+=tempMax-A[i]+1
                tempMax+=1
            else:
                tempMax=A[i]
        return res