# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        lst = [(s.start,s.end) for s in intervals]
        lst.sort()
        if not lst:
            return lst
        ends = [lst[0][1]]
        #starts = [lst[0][1]]
        starts = [lst[0][0]]
        for item in lst[1:]: #注意从第二个数开始
            if item[0]<=ends[-1]:
                ends[-1] = max(ends[-1],item[1])
            else:
                ends.append(item[-1])
                starts.append(item[0])
        return list(zip(starts,ends))
