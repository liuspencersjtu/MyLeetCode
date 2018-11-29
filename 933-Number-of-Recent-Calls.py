class RecentCounter:

    def __init__(self):
        self.time = 0
        self.record=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.time = t
        t1=t-3000
        self.record.append(t)
        #res = 0
        #newRecord = []
        #self.record = [i for i in self.record if i>=t1]
        for i in range(len(self.record)):
            if self.record[i]>=t1:
                break
        self.record=self.record[i:]
        return len(self.record)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)