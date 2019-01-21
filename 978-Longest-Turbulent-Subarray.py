class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lst = []
        N = len(A)
        if not A or N==1:
            return N
        for i in range(N-1): 
            if A[i]<A[i+1]:
                lst.append(1)
            elif A[i]==A[i+1]:
                lst.append(9999999)
            else:
                lst.append(-1)
        N = len(lst)
        lengthMax=1
        s = [lst[0]]
        for i in range(N):
            if lst[i]+s[-1]!=0:
                k=len(s)
                if k>lengthMax:
                    lengthMax=k
                s=[lst[i]]
            else:
                s.append(lst[i])
            k=len(s)
            if k>lengthMax:
                    lengthMax=k
        
            
        return lengthMax+1
