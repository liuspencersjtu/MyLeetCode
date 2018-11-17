class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res1 = []
        res2 = []
        for i in A:
            if i%2==0:
                res1.append(i)
            else:
                res2.append(i)
        return res1+res2