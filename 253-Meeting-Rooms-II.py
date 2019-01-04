from heapq import heappush, heappop
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key = lambda x:x.start)
        end = []
        for it in intervals:
            # if the first finished meeting m1 ends before the next meeting
            # we can directly pop m1, because there is no need to add a new room
            if end and end[0] <= it.start: 
                heappop(end)
            heappush(end, it.end)
            
        return len(end)
