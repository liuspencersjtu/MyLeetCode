class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Solution 1:
        # if not matrix:
        #     return []
        # return list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])
        # Solution 2:
        if matrix == [] : return []
        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix) - 1
        maxRight = len(matrix[0]) - 1
        direction = 0 # 0 right, 1 down, 2 left, 3 up
        while True:
            if direction == 0: # go right
                for i in range(maxLeft, maxRight+1):
                    res.append(matrix[maxUp][i])
                maxUp += 1
            elif direction == 1: # go down
                for i in range(maxUp, maxDown+1):
                    res.append(matrix[i][maxRight])
                maxRight -= 1
            elif direction == 2: #go left
                for i in range(maxRight, maxLeft-1, -1):
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            else: # go up
                for i in range(maxDown, maxUp-1,-1):
                    res.append(matrix[i][maxLeft])
                maxLeft += 1
            if maxUp > maxDown or maxLeft > maxRight:
                return res
            direction = (direction+1)%4
        
