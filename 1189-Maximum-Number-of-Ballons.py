class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        memo = collections.defaultdict(int)
        for a in text:
            memo[a] +=1
        return min(memo['b'], memo['a'], memo['n'], memo['l']//2, memo['o']//2)
                  
