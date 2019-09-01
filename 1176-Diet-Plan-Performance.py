class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        slow, fast = 0, k-1
        cur = sum(calories[slow:fast+1])
        N = len(calories)
        res = 0
        while True:
            if cur<lower:
                res-=1
            elif cur>upper:
                res+=1
            if fast+1<N:
                cur-=calories[slow]
                cur+=calories[fast+1]
                slow, fast = slow+1, fast+1
            else:
                break
        return res
