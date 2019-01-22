class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        valley = prices[0];
        peak = prices[0];
        maxprofit = 0;
        N = len(prices);
        i = 0
        while i<N-1:
            while i<N-1 and prices[i]>=prices[i+1]:
                i+=1
            valley = prices[i]
            while i<N-1 and prices[i]<=prices[i+1]:
                i+=1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit
