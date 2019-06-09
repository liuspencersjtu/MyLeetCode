from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        for i in range(1,len(tiles)+1):
            res.update(permutations(tiles,i))
        #print(res)
        return len(res)
