"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # bfs
        if not node:
            return None
        memo={1:Node(1)}
        stack = [node]
        while stack:
            next_stack = []
            for n in stack:
                for nn in n.neighbors:
                    if nn.val in memo:
                        memo[n.val].neighbors.append(memo[nn.val])
                    else:
                        memo[nn.val] = Node(nn.val)
                        memo[n.val].neighbors.append(memo[nn.val])
                        next_stack.append(nn)
            stack = next_stack
            # print([_.val for _ in stack])
        # print([_.val for _ in memo[1].neighbors])
        return memo[1]                        
