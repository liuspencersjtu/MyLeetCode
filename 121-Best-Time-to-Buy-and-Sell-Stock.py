class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # two pointer,profit holds the biggest profit before current
        # and lowest holds the lowest prices before current
        if len(prices)<=1:
            return 0
        lowest = prices[0]
        profit = 0
        for i in range(len(prices)):
            money = prices[i] - lowest
            if money>profit:
                profit = money
            if prices[i]<lowest:
                lowest = prices[i]
        
        return profit
        
        '''
        # intuitive solution,for every day,search the day before this day
        # and find the lowest price to buy
        profit = {}
        
        if len(prices)<=1:
            return 0
        
        for i in range(len(prices)):
            profit[i] = 0
            for _ in range(i):
                profit[_] = max(profit[_],prices[i]-prices[_])
                
        return max(profit.values())
        '''