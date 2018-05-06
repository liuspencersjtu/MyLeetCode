class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = list(S.lower())
        res = []
        if '@' in s:
            #email
            a = s.index('@')
            for i in range(0,a):
                if i !=0 and i != a-1:
                    pass
                else:
                    res.append(s[i])
            for i in range(5):
                res.insert(1,'*')
            res = res + s[a:]
        else:
            #phone numbers
            ns = []
            for i in s:
                if not (i =='(' or i == ')' or i == ' ' or i == '+' or i == '-'):
                    ns.append(i)
            l = len(ns)
            for i in range(l-1,l-5,-1):
                res.insert(0,ns[i])
            res = list('***-***-') + res
            if l>10:
                res.insert(0,'-')
                res = ['+']+['*']*(l-10)+res
                
        return ''.join(res)