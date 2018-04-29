class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = S.split()
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(s)):
            if s[i][0] in vowel:
                s[i] = s[i]+'ma'
            else:
                s[i] = list(s[i])
                s[i].append(s[i].pop(0))
                s[i] = ''.join(s[i])
                s[i] = s[i]+'ma'
        cnt = 1
        for i in range(len(s)):
            s[i] = s[i] + cnt*'a'
            cnt += 1
        return ' '.join(s)
                