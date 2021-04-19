class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort BFS or DFS is fine
        from collections import defaultdict
        indegrees = defaultdict(int)
        adjacency = defaultdict(list)
        for a,b in prerequisites:
            indegrees[a] += 1
            adjacency[b].append(a)
        # bfs
        res = []
        stack = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                stack.append(i)
        while stack:
            node = stack.pop(0)
            res.append(node)
            for child in adjacency[node]:
                indegrees[child]-=1
                if indegrees[child]==0:
                    stack.append(child)
        if len(res)==numCourses:
            return res
        else:
            return []
