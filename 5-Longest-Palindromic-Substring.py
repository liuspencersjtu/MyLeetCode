class Solution:
    def tryCenter(self, s, center):
        i = 0
        length = len(s)-1
        while center-i>=0 and center+i<=length:
            if s[center-i] != s[center+i]:
                break
            else:
                i += 1
        return 2*i-1
    
    def tryLeft(self, s, left):
        i = 0
        length = len(s)-1
        while left-i>=0 and left+1+i<=length:
            if s[left-i] != s[left+1+i]:
                break
            else:
                i += 1
        return 2*i
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLength = 0
        ans = ''
        for i in range(len(s)):
            tempLength = self.tryCenter(s, i)
            if tempLength > maxLength:
                maxLength = tempLength
                tempLength = int((tempLength-1)/2)
                ans = s[(i-tempLength):(i+1+tempLength)]
            tempLength = self.tryLeft(s, i)
            if tempLength > maxLength:
                maxLength = tempLength
                tempLength = int((tempLength)/2)
                if tempLength>0:
                    ans = s[(i+1-tempLength):(i+1+tempLength)]
        return ans