class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        s=[int(i) for i in S]
        k=sum(s)
        book = {}
        index = 0
        n = len(s)
        for i in range(len(s)):
            if s[i]==1:
                index+=1
                # the index th 1 is in position i
                book[index]=i
        res = [k]
        for item in book:
            #print(item,n,book[item],k)
            res.append(2*item-1+n-book[item]-1-k)
        #if book:
        #    res.append(n-book[1]-1-k+1)
        print(res)
        return min(res)
        