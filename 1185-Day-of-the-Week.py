class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap_year(y):
            if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0)):
                return True
            else:
                return False
        days = 0
        for i in range(1971, year):
            if is_leap_year(i):
                days += 366
            else:
                days += 365
        month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        for mm in range(1,month):
            if mm==2 and is_leap_year(year):
                days += 29
            else:
                days += month_days[mm]
        days += day
        memo = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        return memo[(days-3)%7]
