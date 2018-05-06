class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        if S == '':
            return []
        fast = 0
        slow = 0
        
        while fast<len(S):
            if S[fast] != S[slow]:
                if fast - slow>=3:
                    res.append([slow,fast-1])
                slow = fast
                fast += 1
            else:
                fast += 1
        
        # postprocessing
        if fast - slow>=3:
            res.append([slow,fast-1])
                
        return res