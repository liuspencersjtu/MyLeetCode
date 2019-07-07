class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        begin = [(it[0],1,it[2]) for it in bookings]
        end = [(it[1]+1,0,it[2]) for it in bookings]
        marks = begin+end
        marks.sort()
        cur = 0
        res = [0]*n
        #print(marks)
        N = len(marks)-1
        for i in range(n):
            while marks and marks[0][0]==i+1:
                if marks[0][1]==1:
                    cur+=marks[0][2]
                else:
                    cur-=marks[0][2]
                marks.pop(0)
            res[i]+=cur
            #print(cur)
        return res
            
