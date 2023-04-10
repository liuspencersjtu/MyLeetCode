class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS
        # from collections import defaultdict
        # g = defaultdict(set)
        # cost = dict()
        # for u,v,c in flights:
        #     g[u].add(v)
        #     cost[u,v]=c
        # queue = [[src,0]]
        # visited = dict()
        # visited[src] = 0
        # for _ in range(k+1):
        #     queue_next = []
        #     for node, price in queue:
        #         for child in g[node]:
        #             if child not in visited or price+cost[node,child]<visited[child]:
        #                 queue_next.append([child, price+cost[node,child]])
        #                 visited[child] = price+cost[node,child]
        #     queue = queue_next
        # if dst in visited:
        #     return visited[dst]
        # else:
        #     return -1


        # dijkstra
        from collections import defaultdict
        adj = defaultdict(list)
        for u,v,c in flights:
            adj[u].append([v,c])

        stops = [float('inf')]*n
        import heapq
        pq = [[0, src, 0]]
        while pq:
            temp = heapq.heappop(pq)
            dist, node, steps = temp
            if steps>stops[node] or steps>k+1:
                continue
            stops[node] = steps
            if node == dst:
                return dist
            for a in adj[node]:
                heapq.heappush(pq, [dist+a[1], a[0], steps+1])
        return -1

