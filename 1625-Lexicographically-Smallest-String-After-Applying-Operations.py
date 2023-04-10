class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        queue = deque([s])
        visited.add(s)
        res = '9'*len(s)
        def op_a(s,a):
            s = list(s)
            for i in range(1,len(s),2):
                s[i] = str((int(s[i])+a)%10)
            return ''.join(s)
        def op_b(s,b):
            return s[-b:]+s[:len(s)-b]
        while queue:
            it = queue.popleft()
            if int(it)<int(res):
                res = it
            it = op_a(it,a)
            while it not in visited:
                queue.append(it)
                visited.add(it)
            it = op_b(it,b)
            if it not in visited:
                queue.append(it)
                visited.add(it)
        return res
