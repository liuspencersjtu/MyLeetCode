class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 并差集，并且需要用到 grid[i][j] is a permutation of [0, ..., N*N - 1].这一个条件
        N = len(grid)
        location = {grid[i][j]:(i,j) for i in range(N) for j in range(N)}
        uf = UnionFind(N**2)
        
        for time in range(N**2):
            i, j = location[time]
            for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i, new_j = i+x, j+y
                if 0<=new_i<N and 0<=new_j<N and grid[new_i][new_j] <= time:
                    uf.union(i*N+j, new_i*N+new_j)
                    if uf.connected(0, N**2-1):
                        return time
                    
        
class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.uf = [i for i in range(n)]
        self.size = [1]*n
        
    def find(self, x):
        while x!= self.uf[x]:
            self.uf[x] = self.uf[self.uf[x]]
            x = self.uf[x]
        return x
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.uf[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        self.size[y_root] = 0
        self.count -= 1
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap, seen, res = [(grid[0][0], 0, 0)], set([0,0]), 0
        while True:
            # 这里利用了矩阵中所有元素刚好是0-n**2-1这样一个现状
            # 每次从目前能走到的高度最低的点向外拓展
            T, i, j = heapq.heappop(heap)
            res = max(res, T)
            if i == j == len(grid) - 1:
                return res
            for x,y in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if 0<=x<len(grid) and 0<=y<len(grid) and (x,y) not in seen:
                    seen.add((x,y))
                    heapq.heappush(heap,(grid[x][y],x,y))
