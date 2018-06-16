class MyCalendarTwo:

    def __init__(self):
        self.reservations = []
        self.intersections = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        res = True
        for slot in self.intersections:
            if not (start >= slot[1] or end <= slot[0]):
                res = False
                break
                    
        if res == True:
            for slot in self.reservations:
                if not (start >= slot[1] or end <= slot[0]):
                    self.intersections.append([max(slot[0],start),min(slot[1],end)])
            self.reservations.append([start, end])
        return res


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)