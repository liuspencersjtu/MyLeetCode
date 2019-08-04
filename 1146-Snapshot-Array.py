class SnapshotArray:

    def __init__(self, length: int):
        self.changes = dict()
        self.deltas = []# place dict
        

    def set(self, index: int, val: int) -> None:
        self.changes[index] = val

    def snap(self) -> int:
        self.deltas.append(self.changes)
        self.changes = dict()
        return len(self.deltas)-1

    def get(self, index: int, snap_id: int) -> int:
        res = 0
        for i in range(snap_id,-1,-1):
            if index in self.deltas[i]:
                res = self.deltas[i][index]
                return res
        return res


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
