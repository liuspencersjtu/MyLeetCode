class Solution:
    ## BFS
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        stack = [[0]]
        res = []
        n=len(graph)-1
        while stack:
            newstack = []
            for ways in stack:
                for item in graph[ways[-1]]:
                    if item==n:
                        res.append(ways+[item])
                    else:
                        newstack.append(ways+[item])
            stack = newstack
        return res

class Solution2:
    def allPathsSourceTarget(self, graph):
        
        res = []
        q = []
        q.append([0,[]])
        n = len(graph)
        
        while q:
            tempNode, route = q.pop(0)
            
            if tempNode == n - 1:
                res.append(route + [tempNode])
                continue
            
            for neighbor in graph[tempNode]:
                q.append([neighbor, route + [tempNode]])
        
        return res