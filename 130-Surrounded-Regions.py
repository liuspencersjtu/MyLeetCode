class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        # dfs
        def dfs_mark(i,j):
            if board[i][j] == 'O':
                board[i][j] = 'K'
            for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=ii<m and 0<=jj<n and board[ii][jj] == 'O':
                    dfs_mark(ii,jj)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    dfs_mark(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'K':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
