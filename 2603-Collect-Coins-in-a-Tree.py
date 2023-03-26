class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        # 思路： 1）去掉所有没有硬币的叶子结点所在的完整branch(所以第二段是在while循环)
        #       2）现在所有叶子结点上都有硬币了，删除叶子结点，循环两次
        #       3）剩下的所有edge数量的2倍即为结果
        #       这道题的一个关键点是edges的数量为n-1，这代表图上不存在环，所以到第3步之后从任意点出发回到原点刚好每个edge都被访问两次
        from collections import defaultdict
        indegrees = defaultdict(int)
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1
        
        leaves = [k for k in indegrees if indegrees[k]==1 and coins[k]!=1]
        while leaves:
            leaves_next = []
            if not leaves:
                break
            for k in leaves:
                if not g[k]:
                    assert indegrees[k]==0
                    continue
                node = g[k][0]
                g[k].remove(node)
                g[node].remove(k)
                indegrees[node] -= 1
                indegrees[k] -= 1
                g.pop(k)
                indegrees.pop(k)
                if indegrees[node]==1 and coins[node]!=1:
                    leaves_next.append(node)
            leaves = leaves_next
        
        leaves = [k for k in indegrees if indegrees[k]==1]
        for _ in range(2):
            leaves_next = []
            for k in leaves:
                if not g[k]:
                    continue
                node = g[k][0]
                g[k].remove(node)
                g[node].remove(k)
                indegrees[node] -= 1
                indegrees[k] -= 1
                g.pop(k)
                indegrees.pop(k)
                if indegrees[node]==1:
                    leaves_next.append(node)
            leaves = [k for k in leaves_next if indegrees[k]==1]
        res = 0
        for u in g:
            res += len(g[u])
        return res
