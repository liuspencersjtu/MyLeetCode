'''
Intuition and Algorithm
This problem is similar to: https://www.geeksforgeeks.org/minimum-cost-polygon-triangulation/
We can solved it with Dynamic programming.
DP(pos1,pos2) = min cost of triangulation of vertices from i to j
if (pos2-pos1<2) return 0; //its not possible to get any triangle
else DP(pos1,pos2)= min(DP(pos1,k)+ DP(k,pos2) + Cost(pos1,pos2,k)) ) 
Where Cost(pos1,pos2,k) is the cost of choose triangle with vertices (pos1,pos2,k) and k go from pos1+1 to pos2-1
'''
from functools import lru_cache
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        #memo = {}
        # just remember to tinker the maxsize of lru_cache
        # the default is 128?
        @lru_cache(4096)
        def dp(pos1, pos2):
            #if (pos1,pos2) in memo:
            #    return memo[(pos1,pos2)]
            #print(pos1,pos2)
            if pos2-pos1<2:
                return 0
            res = float('inf')
            for k in range(pos1+1,pos2):
                res = min(res, dp(pos1,k)+dp(k,pos2)+A[pos1]*A[pos2]*A[k])
            #memo[(pos1,pos2)]=res
            return res
        res = dp(0,len(A)-1)
        return res
