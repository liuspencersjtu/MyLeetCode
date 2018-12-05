class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        i=1
        while 2**i-1<num:
            i+=1
        board = [0,1]
        for k in range(1,i):
            board = board + [i+1 for i in board]
        return board[:num+1]
