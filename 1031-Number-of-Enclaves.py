class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        def shrink(A,i,j):
            ##
            if not (0<=i<M and 0<=j<N):
                return
            if A[i][j]==0:
                return
            A[i][j]=0
            for i1, j1 in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                ##
                shrink(A,i1,j1)
        for i in range(M):
            shrink(A,i,0)
            shrink(A,i,N-1)
        for j in range(N):
            shrink(A,0,j)
            shrink(A,M-1,j)
        return sum([sum(it) for it in A])
