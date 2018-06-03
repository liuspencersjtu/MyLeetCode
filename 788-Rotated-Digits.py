class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        table = {0:1,1:1,8:1,2:2,5:2,6:2,9:2,3:3,4:3,7:3}
        #l2 = {2:1,5:1,6:1,9:1}
        #l3 = {3:1,4:1,7:1}
        res = 0
        for i in range(1,N+1):
            content = list(str(i))
            a, b, c = 0,0,0
            for k in content:
                t = table[int(k)]
                if t == 1:
                    a+=1
                elif t == 2:
                    b+=1
                else:
                    c+=1
            if c != 0:
                continue
            elif b != 0:
                res += 1
        return res
                
                
            