class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # time O(N) space O(N)
        if not intervals or len(intervals) == 0:
            return [newInterval]
        idx = -1
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                idx = i
                break
        if idx != -1:
            intervals.insert(i, newInterval)
        else:
            intervals.append(newInterval)
        res = []
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res
