class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = collections.defaultdict()
        a = ord('a')
        for i in range(len(words_morse)):
            alphabet[chr(a+i)]=words_morse[i]
        transformation = set()
        #print(alphabet)
        def trans(word):
            res = []
            for i in word:
                #print(i)
                res.append(alphabet[i])
            return ''.join(res)
        for i in words:
            transformation.add(trans(i))
        return len(transformation)