class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M,N = len(board), len(board[0])
        def dfs(i,j, word):
            if not word:
                return True
            if board[i][j] != word[0]:
                return False
            if len(word)==1 and board[i][j]==word[0]:
                return True
            # restrain
            tmp = board[i][j]
            board[i][j] = '*'
            for m,n in [(i-1,j), (i+1,j), (i, j-1), (i, j+1)]:
                if 0<=m<M and 0<=n<N and dfs(m,n, word[1:]):
                    return True
            board[i][j] = tmp
            return False
        for i in range(M):
            for j in range(N):
                if dfs(i,j, word):
                    return True
        return False
