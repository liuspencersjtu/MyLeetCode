class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        a = ord('a')
        s = [ord(i)-a for i in list(S)]
        times = sum(shifts)
        shifts.insert(0,0)
        for i in range(len(s)):
            times = times - shifts[i]
            m = (times + s[i])%26
            s[i] = chr(a+m)
        return ''.join(s)