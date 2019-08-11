class Solution:
    def dayOfYear(self, date: str) -> int:
        def specialYear(y):
            if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0)):
                return True
            else:
                return False
        memo = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
        specialmemo = {1:0,2:31,3:60,4:91,5:121,6:152,7:182,8:213,9:244,10:274,11:305,12:335}
        date = list(map(int,date.split('-')))
        if specialYear(date[0]):
            return specialmemo[date[1]]+date[2]
        else:
            return memo[date[1]]+date[2]
        
