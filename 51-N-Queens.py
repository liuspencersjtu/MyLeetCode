class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        "Initial chessboard with 0"
        chess_board = []
        for i in range(n):
            line = []
            for j in range(n):
                line.append(0)
            chess_board.append(line)
            
        solution = []
        
        def checkLine(i,j):
            result = 1
            for k in range(i):
                if chess_board[k][j] == 1:
                    result = 0
            return result
        
        def checkPolygon(i,j):
            result = 1
            step = 1
            while i + step < n and j + step <n:
                if chess_board[i+step][j+step] == 1:
                    result = 0
                step += 1
            step = 1
            while i + step < n and j - step >= 0:
                if chess_board[i+step][j-step] == 1:
                    result = 0
                step += 1
            step = 1
            while i - step >= 0 and j + step < n:
                if chess_board[i-step][j+step] == 1:
                    result = 0
                step += 1
            step = 1
            while i - step >= 0 and j - step >= 0:
                if chess_board[i-step][j-step] == 1:
                    result = 0
                step += 1
            return result
        
        def collectSolution():
            this_solution = []
            dic = {0:'.',1:'Q'}
            for i in range(n):
                s=''
                for j in range(n):
                    s += dic[chess_board[i][j]]
                this_solution.append(s)
            solution.append(this_solution)
            
        def cleanBoard():
            for i in range(n):
                for j in range(n):
                    chess_board[i][j] = 0
            
        if n == 1:
            solution = [['Q']]
        
        for k in range(n):
            chess_board[0][k] = 1
            # assume this placement can lead to a solution
            reach_end = 0
            # for row
            for i in range(1,n):
                # for column
                for j in range(n):
                    # if already reach end, then we don't need to proceed
                    if reach_end:
                        break
                    chess_board[i][j] = 1
                    if checkLine(i,j) and checkPolygon(i,j):
                        if i == (n-1):
                            collectSolution()
                            # when we need to run this line of code, it means we are at the last row and find a solution
                            # then we clean the board and the program will jump to first line and try the second solution
                            cleanBoard()
                            reach_end = 1
                            
                            # return to the prior state
                            # chess_board[i][j] = 0
                        else:
                            # if this is not the last row then break to search the next
                            break
                    else:
                        # if this grid does not fit, then clean this grid and go the next grid in this column
                        chess_board[i][j] = 0
                        # if all grid in this row does not fit, then reprot no_solution for the primary setting
                        if j == (n-1):
                            reach_end = 1
                            cleanBoard()
            chess_board[0][k] = 0
            
        return solution