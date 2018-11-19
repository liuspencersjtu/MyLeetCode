class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        #stack only contains '('
        stack=[]
        res = 0
        for i in S:
            if i==')':
                if stack:
                    stack.pop()
                    res-=1
                else:
                    res+=1
            else:
                stack.append(i)
                res+=1
        return res