class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ''
        if B<=A<=2*B:
            return 'aab'*(A-B)+'ab'*(2*B-A)
        elif A>=2*B:
            return 'aab'*B+'a'*(A-2*B)
        elif A<=B<=2*A:
            return 'bba'*(B-A)+'ba'*(2*A-B)
        elif B>=2*A:
            return 'bba'*A+'b'*(B-2*A)
        else:
            return ''
