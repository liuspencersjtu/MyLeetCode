class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def helper(word1, word2, alphabet):
            n1 = len(word1)
            n2 = len(word2)
            i=0
            while i<min(n1,n2):
                if word1[i] == word2[i]:
                    i+=1
                else:
                    if alphabet.index(word1[i])<alphabet.index(word2[i]):
                        return True
                    else:
                        return False
        for i in range(len(words)-1):
            if not helper(words[i],words[i+1],order):
                return False
        return True
