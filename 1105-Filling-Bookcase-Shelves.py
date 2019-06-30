from functools import lru_cache
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N = len(books)
        @lru_cache(1000)
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return books[0][1]
            total_height = float('inf')
            level_height = 0
            level_thick = 0
            k=1
            while i-k>=0:
                level_height =max(level_height,books[i-k][1])
                level_thick += books[i-k][0]
                if level_thick>shelf_width:
                    break
                total_height = min(total_height,level_height+dp(i-k))
                k+=1
            return total_height
        return dp(N)
