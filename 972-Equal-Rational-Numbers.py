class Solution:
    # A cheating solution
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def help(a):
            i=a.find('(')
            b=a
            if i>=0:
                b=a[:i]+a[i+1:-1]*20
                return float(b[:30])
            return float(b)
        return help(S)==help(T)
