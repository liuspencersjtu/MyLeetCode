class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        self.cash = {5:0,10:0,20:0}
        #def case1():
        #    if self.cash.get(5) == 0:
        #strategy = {5:case1, 10:case2, 15:case3}
        for bill in bills:
            if bill == 5:
                self.cash[5] += 1
            elif bill == 10:
                if self.cash.get(5) == 0:
                    return False
                else:
                    self.cash[5] -= 1
                    self.cash[10] += 1
            else:
                # bill == 20
                if self.cash[10] == 0:
                    if self.cash[5] < 3:
                        return False
                    else:
                        self.cash[5] -= 3
                        self.cash[20] += 1
                else:
                    if self.cash[5] == 0:
                        return False
                    else:
                        self.cash[10] -= 1
                        self.cash[5] -= 1
                        self.cash[20] += 1
        return True