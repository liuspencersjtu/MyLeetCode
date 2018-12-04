class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r1,c1=a.split('+')
        r1 = int(r1)
        c1 = int(c1[:-1])
        r2,c2=b.split('+')
        r2 = int(r2)
        c2 = int(c2[:-1])
        r3 = r1*r2-c1*c2
        c3 = r1*c2+r2*c1
        return '{}+{}i'.format(r3,c3)
