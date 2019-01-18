class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x%10==0 and x!=0:
            return False
        a=0
        while x>a:
            b = x%10
            a=a*10+b
            x=x//10
        return bool(x==a or a//10==x)
        '''
        x=str(x)
        N = len(x)
        for i in range(N//2):
            if x[i] !=x[N-1-i]:
                return False
        return True
        '''
