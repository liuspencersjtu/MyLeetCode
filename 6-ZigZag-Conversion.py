class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['']*min(numRows, len(s))
        curRow = 0
        goingDown = False
        for c in s:
            #
            rows[curRow] = rows[curRow]+c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow = curRow+1 if goingDown else curRow-1
        return ''.join(rows)
