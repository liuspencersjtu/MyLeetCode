class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        b = defaultdict(int)
        for item in A:
            if b[item]!=0:
                return item
            else:
                b[item]+=1
