class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = list(map(lambda x:x.replace('/', ''), path))
        path =list(filter(lambda x: (x!='' and x!='.'), path))
        res = []
        for p in path:
            if p == '..':
                if res:
                    res.pop()
                continue
            res.append(p)
        return '/'+'/'.join(res)
