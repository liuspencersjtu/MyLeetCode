class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9+7
        from collections import defaultdict, Counter
        dp = defaultdict(Counter)
        dp[(0,0)][grid[0][0]%k]=1 # think of this as before enter 0,0 and carry 0 as intial value
        for i in range(m):
            for j in range(n):
                if i>0:
                    for c in dp[(i-1,j)]:
                        dp[(i,j)][(c+grid[i][j])%k] += dp[(i-1,j)][c]
                if j>0:
                    for c in dp[(i,j-1)]:
                        dp[(i,j)][(c+grid[i][j])%k] += dp[(i,j-1)][c]
        return dp[(m-1,n-1)][0]%(10**9+7)
#   this top-down is too slow yet correct
#   cannot use backtracking?
#         # self.res = 0
#         self.k = k
#         self.hashmap = {}
#         m, n = len(grid), len(grid[0])
#         def helper(i,j,s):
#             if (i,j,s) in self.hashmap:
#                 return self.hashmap[(i,j,s)]
#             if i==m-1 and j==n-1:
#                 if (s+grid[m-1][n-1])%self.k==0:
#                     self.hashmap[(i,j,s)]=1
#                     return self.hashmap[(i,j,s)]
#                 else:
#                     self.hashmap[(i,j,s)]=0
#                     return self.hashmap[(i,j,s)]
#             res = 0
#             if i<m-1:
#                 res += helper(i+1,j,(s+grid[i][j])%self.k)
#             if j<n-1:
#                 res += helper(i,j+1,(s+grid[i][j])%self.k)
#             self.hashmap[(i,j,s)] = res%(10**9+7)
#             return self.hashmap[(i,j,s)]
            
#         self.res = helper(0,0,0)
#         return self.res%(10**9+7)
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/discuss/2678950/Python-DP-solution
