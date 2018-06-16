class MyCalendar:

    def __init__(self):
        self.reservations = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        res = True
        for slot in self.reservations:
            if not (start>=slot[1] or end<=slot[0]):
                res = False
                break
        if res == True:
            self.reservations.append([start,end])
        return res


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# Another solution
from bisect import bisect
class MyCalendar:

    def __init__(self):
        self.dic={float('-Inf'):float('-Inf'),float('Inf'):float('Inf')}
        self.nums=[float('-Inf'),float('Inf')]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i=bisect(self.nums,start)
        if start<self.dic[self.nums[i-1]] or end>self.nums[i]:
            return False
        self.nums.insert(i,start)
        self.dic[start]=end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)