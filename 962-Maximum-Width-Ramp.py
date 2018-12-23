class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N=50001
        sms = [None]*N
        lgs = [None]*N
        # record the smallest and the largest index of each value
        for i,x in enumerate(A):
            if sms[x]==None:
                sms[x]=i
            lgs[x]=i
        # ss is the global minimum index of value smaller than the current number x
        ss=float('inf')
        res = 0
        for x in range(N):
            if sms[x]==None:
                continue
            ss = min(ss,sms[x])
            res = max(res, lgs[x]-ss)
            
        return res
            
        
