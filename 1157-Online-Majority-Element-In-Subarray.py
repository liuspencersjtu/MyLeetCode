class MajorityChecker:

    def __init__(self, arr: List[int]):
        a2l = collections.defaultdict(list)
        for i,a in enumerate(arr):
            a2l[a].append(i)
        self.arr = arr
        self.a2l = a2l
        

    def query(self, left: int, right: int, threshold: int) -> int:
        # use bisect to find it
        # since the element is the majority
        for _ in range(20):
            a = self.arr[random.randint(left,right)]
            indices = self.a2l[a]
            l = bisect.bisect_left(indices, left)
            r = bisect.bisect_right(indices, right)
            if r-l >= threshold:
                return a
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
