class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return True
        d1 = list(sorted(str(N)))
        for i in range(1, 33):
            d2 = list(sorted(str(1 << i)))
            if d1 == d2:
                return True
        return False
    '''
    def twoPower(self, N):
        i = 1
        while i<=N:
            if i == N:
                return True
            else:
                i = i*2
        return False
    
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        from itertools import permutations
        import math
        n = str(N)
        #length = len(n)
        p = permutations(n)
        for item in p:
            if item[0] != '0':
                num = int(''.join(item))
                if self.twoPower(int(''.join(item))):
                    return True
                #N = int(''.join(item))
                #n = math.log(N, 2)
                #if n == round(n):
                #    return True
        return False
    '''