class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isWordEnd = False
        
    def buildTrie(self, words):
        for word in words:
            curr = self
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWordEnd = True
            
    def find(self, word, curr = None):
        if not curr:
            curr = self
        for i, char in enumerate(word):
            if char == '.':
                for child in curr.children:
                    if self.find(word[i+1:], curr.children[child]):
                        return True
                else:
                    return False
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWordEnd
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        self.trie.buildTrie([word])

    def search(self, word: str) -> bool:
        return self.trie.find(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
