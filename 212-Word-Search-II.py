class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isWordEnd = False
        
    def buildTrie(self, words):
        for word in words:
            curr = self
            for char in word:
                if char not in curr.children:#这个if不能少
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWordEnd = True
            
    def find(self, word, curr=None):
        if not curr:
            curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True      
        
class Solution:
    # 复杂度太高，需要计算所有可能的word，同样使用trie应该只考虑构建words中有的词
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # dfs 所有位置，把结果存到trie里
        PossibleWords = []
        M, N = len(board), len(board[0])
        visited = [[False]*N for _ in range(M)]
        def dfs(word, i, j):
            word += board[i][j]
            PossibleWords.append(word)
            visited[i][j] = True
            for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=m<M and 0<=n<N and not visited[m][n]:
                    dfs(word,m,n)
            visited[i][j] = False
        for i in range(M):
            for j in range(N):
                dfs('', i, j)
        trie = TrieNode()
        trie.buildTrie(PossibleWords)
        res = []
        for word in words:
            if trie.find(word):
                res.append(word)
        return res
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        trie.buildTrie(words)
        M, N = len(board), len(board[0])
        res = []
        def dfs(i, j, node, path):
            # if node.isWordEnd == True:
            #     res.append(path)
            if board[i][j] not in node.children:
                return 
            elif node.children[board[i][j]].isWordEnd == True:
                res.append(path+board[i][j])
                return
            for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=m<M and 0<=n<N:
                    dfs(m,n,node.children[board[i][j]],path+board[i][j])
        for i in range(M):
            for j in range(N):
                dfs(i,j,trie,'')
        return res
