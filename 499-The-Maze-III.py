class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        dest=tuple(hole)
        m=len(maze)
        n=len(maze[0])
        direc = {(1, 0):'d', (0,-1):'l', (0,1):'r', (-1, 0):'u'}
        
        def go(start, direction, path):
            i, j = start
            ii, jj = direction
            l=0
            while 0<=i+ii<m and 0<=j+jj<n and maze[i+ii][j+jj]!=1:
                i+=ii
                j+=jj
                l+=1
                if i==dest[0] and j==dest[1]:
                    return l, (i,j), path+direc[direction]
            if l>0:
                return l, (i,j), path+direc[direction]
            else:
                return l, (i,j), path
        
        visited={}
        q=[]
        heapq.heappush(q, (0, tuple(ball),''))
        while q:
            length, cur, path = heapq.heappop(q)
            if path:
                visited[(cur,path[-1])]=length
            if cur == dest:
                print(length)
                return path
            for direction in direc:
                #print(cur, direction, path,go(cur, direction, path))
                l, np, newpath = go(cur, direction, path)
                if newpath and (np, newpath[-1]) not in visited: # visited 过的点，不压队列。
                    heapq.heappush(q, (length+l, np, newpath))
        return 'impossible'
