class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        memo = {}
        for i in range(len(S)):
            if memo.get(S[i],0)==0:
                memo[S[i]]=[i,i]
            else:
                memo[S[i]][1]=i
        nodes=[]
        for item in memo.values():
            nodes.append([item[0],0])
            nodes.append([item[1],1])
        nodes.sort(key=lambda x:x[0])
        stack=[]
        res=[]
        for item in nodes:
            if item[1]==1:
                temp=stack.pop()
                if not stack:
                    res.append(item[0]-temp[0]+1)
            else:
                stack.append(item)
        return res