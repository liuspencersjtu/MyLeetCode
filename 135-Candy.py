class Solution:
    def candy(self, ratings: List[int]) -> int:
        fromleft = []
        if len(ratings) == 1:
            return 1
        fromleft.append(1)
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                fromleft.append(fromleft[-1]+1)
            else:
                fromleft.append(1)
        fromright = [1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                fromright.append(fromright[-1]+1)
            else:
                fromright.append(1)
        fromright = fromright[::-1]
        res = 0
        # print(fromleft,fromright)
        for i in range(len(fromleft)):
            res += max(fromleft[i],fromright[i])
        return res
        
