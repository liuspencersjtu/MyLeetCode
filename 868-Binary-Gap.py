class Solution:
    def toBinary(self, N):
        #ans = 0
        ans = []
        #n = 0
        while N>0:
            #ans = ans+(N%2)*(10**n)
            ans.insert(0, N%2)
            #n += 1
            N = N//2
        return ans
    
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary_N = self.toBinary(N)
        gap = 0
        slow, fast = 0, 0
        length = len(binary_N)-1
        while fast <= length:
            if binary_N[fast] == 1:
                if slow < fast:
                    if binary_N[slow] == 1:
                        gap = max(gap, fast-slow)
                    slow = fast
                else:
                    fast += 1
            else:
                fast += 1
        '''        
        if slow != fast-1:
            if binary_N[slow] == 1 and binary_N[fast-1] == 1:
                gap = max(gap, fast - slow)
        '''
        return gap
        