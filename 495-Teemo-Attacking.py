class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        if len(timeSeries)<2:
            if not timeSeries:
                return 0
            else:
                return duration
        for i in range(1,len(timeSeries)):
            res += min(duration, timeSeries[i]-timeSeries[i-1])
        return res+duration