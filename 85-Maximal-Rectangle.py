class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 需要结合第84题来做
        if not matrix:
            return 0
        else:
            A = [0]*len(matrix[0])
        def largestRect(A):
            # mono stack increase 存位置
            B = [0] + A + [0]
            # print(B)
            stack = []
            res = 0
            for i, num in enumerate(B):
                while stack and B[stack[-1]]>num:
                    height = B[stack.pop()]
                    if stack:
                        res = max(res, (i-stack[-1]-1)*height)
                stack.append(i)
            return res
        res = 0
        for line in matrix:
            for i in range(len(line)):
                A[i] = A[i]*int(line[i]) + int(line[i])
            res = max(res, largestRect(A))
        return res
