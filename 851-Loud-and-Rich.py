class Solution:
    def dfs(self, x):
        if self.ret[x] is not None:
            return

        # print(x, self.edge[x])

        self.ret[x] = x
        for i in self.edge[x]:
            self.dfs(i)
            if self.q[self.ret[i]] < self.q[self.ret[x]]:
                self.ret[x] = self.ret[i]

    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        #import collections

        self.q = quiet
        self.n = len(quiet)
        #self.edge = [collections.deque() for _ in range(self.n)]
        self.edge = [[] for _ in range(self.n)]
        for (p, q) in richer:
            self.edge[q].append(p)

        self.ret = [None for _ in range(self.n)]
        for i in range(self.n):
            self.dfs(i)
        return self.ret