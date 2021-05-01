class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # mono stack 单调栈
        stack = [] #单调增,这样我们可以轻松找出比当前高度小的最后一个位置
        heights = [0] + heights + [0]
        res = 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]]>height:
                curr = stack.pop()
                # 这时候stack[-1] 和 i 变成了curr这个位置左右的两个边界
                res = max(res, (i-stack[-1]-1)*heights[curr])
            stack.append(i)
        return res
