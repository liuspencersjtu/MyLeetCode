class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<=2:
            res={0:[],1:[[1]],2:[[1],[1,1]]}
            return res[numRows]
        res = [[1],[1,1]]
        temp1 = [1,1]
        for i in range(3,numRows+1):
            temp2 = [1]
            for i in range(1,len(temp1)):
                temp2.append(temp1[i-1]+temp1[i])
            temp2.append(1)
            res.append(temp2)
            temp1=temp2
        return res
