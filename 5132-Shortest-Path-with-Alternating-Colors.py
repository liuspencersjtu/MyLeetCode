from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        for k,v in red_edges:
            red[k].append(v)
        blue = defaultdict(list)
        for k,v in blue_edges:
            blue[k].append(v)
        res = [-1]*n
        res[0] = 0
        step = 0
        queue = [(0,0),(0,1)]# 0,red and 0, blue
        length = min(len(red),len(blue))*2+2
        visited_blue = set([0])
        visited_red = set([0])
        while queue and step<2*n+2:
            step+=1
            newqueue = []
            for it, _ in queue:
                if _ == 0:#red
                    if it in blue:
                        for v in blue[it]:
                            if v not in visited_blue:
                                newqueue.append((v,1))
                                visited_blue.add(v)
                            if res[v] == -1:
                                res[v] = step
                if _ == 1:
                    if it in red:
                        for v in red[it]:
                            if v not in visited_red:
                                newqueue.append((v,0))
                                visited_red.add(v)
                            if res[v] == -1:
                                res[v] = step
            queue = newqueue
        return res
