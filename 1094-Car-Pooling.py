class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickup = [(it[1],1,it[0]) for it in trips]
        dropoff = [(it[2],0,it[0]) for it in trips]
        points = pickup+dropoff
        points.sort()
        cur = 0
        for it in points:
            if it[1] == 0:
                cur-=it[2]
            else:
                cur+=it[2]
                if cur > capacity:
                    return False
        return True
