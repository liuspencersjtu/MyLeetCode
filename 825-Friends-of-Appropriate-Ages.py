class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        #Two pointer
        #ages.sort()
        aas = list(set(ages))
        aas.sort()
        temp = []
        best = 0
        res = 0
        for a in aas:
            if a<=14:
                continue
            while (temp and temp[0] <= 0.5*a+7):
                temp.pop(0)
            n = ages.count(a)
            res += (len(temp)+n-1)*n
            temp = temp + [a]*n
            
        return res