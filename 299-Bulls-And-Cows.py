class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        bull, cow = 0, 0
        guess = list(guess)
        secret = list(secret)
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
                secret[i] = 'x'
                guess[i] = 'y'
        from collections import defaultdict
        secretDict = defaultdict(int)
        for i in range(n):
            secretDict[secret[i]] += 1
        for item in guess:
            if secretDict.get(item, 0)>0:
                secretDict[item] -= 1
                cow += 1
        return str(bull)+'A'+str(cow)+'B'
            