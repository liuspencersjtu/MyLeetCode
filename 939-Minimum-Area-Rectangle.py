class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0
        '''
        xs = collections.defaultdict()
        ys = collections.defaultdict()
        for item in points:
            xs[item[0]] = xs[item[0]]+1
            ys[item[1]] = ys[item[1]]+1
        axis0 = []
        axis1 = []
        for i in xs:
            if xs[i]>1:
                axis0.append(i)
        for i in ys:
            if ys[i]>1:
                axis1.append(i)
        '''