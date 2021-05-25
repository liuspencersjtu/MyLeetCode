class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        for i, line in enumerate(triangle):
            if i == 0:
                continue
            line[0] += triangle[i-1][0]
            for j in range(1, len(line)-1):
                line[j] += min(triangle[i-1][j-1], triangle[i-1][j])
            line[-1] += triangle[i-1][-1]
        return min(triangle[-1])
