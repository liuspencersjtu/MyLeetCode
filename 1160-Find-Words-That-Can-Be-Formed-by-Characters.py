class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        memo = collections.Counter(chars)
        res = 0
        for word in words:
            memo1 = collections.Counter(word)
            check = True
            for it in memo1:
                if it not in memo or memo[it]<memo1[it]:
                    check = False
                    break
            if check:
                res += len(word)
        return res
