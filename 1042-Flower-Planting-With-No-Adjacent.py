import collections
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        ## greedy algorithm
        res = [0]*N
        connect = collections.defaultdict(list)
        for a,b in paths:
            connect[a].append(b)
            connect[b].append(a)
        for i in range(1,N+1):
            res[i-1] = ({1,2,3,4} - {res[it-1] for it in connect[i]}).pop()
        return res
