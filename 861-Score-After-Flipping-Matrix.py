class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def flip(a):
            for i in range(len(a)):
                if a[i]==1:
                    a[i]=0
                else:
                    a[i]=1
        for item in A:
            if item[0]==0:
                flip(item)
        b=list(zip(*A))
        n=len(A[0])-1
        res = 0
        for item in b:
            #print(item)
            res+=(2**n)*max(item.count(0),item.count(1))
            n-=1
        return res