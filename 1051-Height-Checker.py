class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct = list(heights)
        correct.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i] != correct[i]:
                res += 1
        return res
