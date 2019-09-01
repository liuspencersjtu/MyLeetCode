import itertools
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 因为puzzles[i].length == 7， 所以先对words和puzzles进行某种格式的记忆之后
        # 遍历puzzle， 每个puzzle对应的可能最多只有2**7，而不需要遍历整个words了。
        # 这是本题的关键。
        # 那么按照这个思路，最开始我们应该记住同一类型的words的个数
        def alphabet(word):
            res = 0
            for w in word:
                res |= 1<<(ord(w)-ord('a'))
            return res
        words = [''.join(sorted(set(word))) for word in words if len(set(word))<=7]
        memo = collections.defaultdict(int)
        for word in words:
            alpha = word
            for w in word:
                memo[(alphabet(w), alpha)]+=1
        
        puzzles = [[1<<(ord(puzzle[0])-ord('a')),puzzle] for puzzle in puzzles]
        answer = []
        def helper(head,puzzle):
            res = 0
            for i in range(1,8):
                for p in itertools.combinations(puzzle, i):
                    res += memo[(head, ''.join(sorted(p)))]
            return res
        for head, puzzle in puzzles:
            answer.append(helper(head, puzzle))
        return answer
