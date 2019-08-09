class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        board = [[0]*n for i in range(n)]
        def helper(i, board):
            for j in range(n):
                if check(i,j):
                    if i == n-1:
                        self.res+=1
                        continue
                    else:
                        board[i][j]=1
                        helper(i+1, board)
                        board[i][j]=0
        def check(i,j):
            for m in range(n):
                if board[m][j]==1:
                    return False
                if board[i][m]==1:
                    return False
            for m in range(i+j+1):
                if 0<=m<n and 0<=i+j-m<n and board[m][i+j-m]==1:
                    return False
            step = 0
            while i-step>=0 and j-step>=0:
                if board[i-step][j-step]==1:
                    return False
                step+=1
            step = 0
            while i+step<n and j+step<n:
                if board[i+step][j+step]==1:
                    return False
                step+=1
            return True
        helper(0, board)
        return self.res
