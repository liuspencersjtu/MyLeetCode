class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [[r0,c0]]
        maxstep = max(r0+c0,r0+C-c0,R-r0+c0,R-r0+C-c0)
        for i in range(1,maxstep+1):
            for a in range(1,i+1):
                b = i-a
                r1 = r0+a
                c1 = c0+b
                if 0<=r1<R and 0<=c1<C:
                    res.append([r1,c1])
            for a in range(i):
                b = i-a
                r1 = r0+a
                c1 = c0-b
                if 0<=r1<R and 0<=c1<C:
                    res.append([r1,c1])
            for a in range(i):
                b = i-a
                r1 = r0-a
                c1 = c0+b
                if 0<=r1<R and 0<=c1<C:
                    res.append([r1,c1])
            for a in range(1,i+1):
                b = i-a
                r1 = r0-a
                c1 = c0-b
                if 0<=r1<R and 0<=c1<C:
                    res.append([r1,c1])
        return res
                    
