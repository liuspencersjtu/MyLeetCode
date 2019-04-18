class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            tmp = set()
            for it in line:
                if it not in tmp:
                    tmp.add(it)
                elif it != '.':
                    print(line)
                    return False
        for i in range(9):
            tmp = set()
            for line in board:
                if line[i] not in tmp:
                    tmp.add(line[i])
                elif line[i] != '.':
                    print(tmp, line[i])
                    return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                tmp = set()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] not in tmp:
                            tmp.add(board[i+m][j+n])
                        elif board[i+m][j+n] != '.':
                            print(i,j)
                            return False
                        
        return True
