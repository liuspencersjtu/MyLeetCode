class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        upperB = int(c**0.5)+1
        
        for i in range(0, upperB):
            
            testV = (c - i*i)**0.5
            
            if testV % 1 == 0:
                return True
            
        return False