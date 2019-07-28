from collections import defaultdict
# 想多了。。把题目理解成了怎样打出target中的字母，但不要求按照顺序，最短是怎样。。。凑合写写吧。。
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        base = ord('a')
        def distance(a:int,b:int):
            x1, y1 = (a-base)//5, (a-base)%5
            x2, y2 = (b-base)//5, (b-base)%5
            return abs(x1-x2)+abs(y1-y2)
        def path(a,b):
            x1, y1 = (a-base)//5, (a-base)%5
            x2, y2 = (b-base)//5, (b-base)%5
            res = ''
            if x2 == (ord('z')-base)//5:
                if y1<y2:
                    res+='R'*(y2-y1)
                if y1>y2:
                    res+='L'*(y1-y2)
                if x2>x1:
                    res+='D'*(x2-x1)
                if x2<x1:
                    res+='U'*(x1-x2)
            elif x1 == (ord('z')-base)//5:
                if x2>x1:
                    res+='D'*(x2-x1)
                if x2<x1:
                    res+='U'*(x1-x2)
                if y1<y2:
                    res+='R'*(y2-y1)
                if y1>y2:
                    res+='L'*(y1-y2) 
            else:   
                if x2>x1:
                    res+='D'*(x2-x1)
                if x2<x1:
                    res+='U'*(x1-x2)
                if y1<y2:
                    res+='R'*(y2-y1)
                if y1>y2:
                    res+='L'*(y1-y2)
            return res
        target = target
        chars = list(set('a'+target))
        N = len(chars)
        # t = [[0]*(N) for _ in range(N)]
        t = defaultdict(lambda :defaultdict(int))
        for i in chars:
            for j in chars:
                t[i][j] = distance(ord(i),ord(j))
        k = 'a'
        res = ''
        # print(t,path(ord('a'),ord('j')))
        target = list(target)
        while target:
            # cur = float('inf')
            # idx = 0
            # for i in range(len(target)):
            #     if t[k][target[i]]<cur:
            #         cur = t[k][target[i]]
            #         idx = i
            # knext = t[k].index(min(t[k][:k]+t[k][k+1:]))
            knext = target[0]
            # print(target[k],target[knext] )
            res += path(ord(k),ord(knext))+'!'
            target.pop(0)
            k = knext
        return res
