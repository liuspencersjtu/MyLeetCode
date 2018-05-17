class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        l = len(s)-1
        i=0
        while i <= l:
            if i <l and dic.get(s[i:i+2],0) != 0:
                res += dic.get(s[i:i+2])
                i += 2
            else:
                res += dic.get(s[i])
                i += 1
        return res