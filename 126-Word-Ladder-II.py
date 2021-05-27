class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        stack = [[beginWord]]
        visited = set([beginWord])
        lookup = set(wordList)
        while stack:
            next_stack = []
            visited_this_stage = []
            for path in stack:
                if path[-1] == endWord:
                    res.append(path)
            if res:
                return res
            for path in stack:
                word = path[-1]
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        trans_word = word[:i] + char + word[i+1:]
                        if trans_word not in visited and trans_word in lookup:
                            visited_this_stage.append(trans_word)
                            next_stack.append(path+[trans_word])
            visited.update(visited_this_stage)
            stack = next_stack
        return []
