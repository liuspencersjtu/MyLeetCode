class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # ### 先写一个o(n**2)的解法，直接对应每个vertex构建树dfs统计正确guess数
        # from collections import defaultdict
        # from functools import lru_cache
        # graph = defaultdict(list)
        # for x,y in edges:
        #     graph[x].append(y)
        #     graph[y].append(x)
        # guesses = set((x,y) for x,y in guesses)
        # @lru_cache(202300)#cache小了的话会超时
        # def get_correct_pairs(x, parent):
        #     res = 0
        #     for child in graph[x]:
        #         if child == parent:
        #             continue
        #         else:
        #             if (x, child) in guesses:
        #                 res += 1
        #             res += get_correct_pairs(child,x)
        #     return res
        # res = 0
        # for node in graph:
        #     if get_correct_pairs(node, None)>=k:
        #         res += 1
        # return res
        
        
        
        
        # 再写一个o(n)的解法
        
        # 从0开始dfs,计算每个中间节点和0的距离d，和dfs得到的0为root时
        # 的正确猜测数cnt，那么中间距离为d的节点正确的猜测数就为cnt+d
        # 距离d的定位是当前节点到0节点路径上正确的预测数-错误的预测数
        from collections import defaultdict
        from functools import lru_cache
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        A = defaultdict(int)
        for x,y in guesses:
            A[(x,y)] = 1
        # here d in the logical distance from node 0 to node x
        # and d = #of wrong guesses - #of correct guesses
        distance = defaultdict(int) #distance[node] = d
        def dfs(x, parent=None, d=0):
            # store distance during travesal, and return correct number
            # of guesses start with node x
            distance[x] = d
            cnt = 0
            for child in graph[x]:
                if child ==parent:
                    continue
                cnt += A[(x,child)]
                cnt += dfs(child, x, d+A[(child,x)]-A[(x,child)])
            return cnt
        cnt = dfs(0) #计算0为root正确的guess数
        res = 0
        for x in graph:
            if cnt+distance[x]>=k:
                res += 1
        return res
