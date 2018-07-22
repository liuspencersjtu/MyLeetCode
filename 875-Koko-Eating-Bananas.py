class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        import math
        k = math.ceil(sum(piles)/H)
        total = 0
        while True:
            total = 0
            for item in piles:
                total += math.ceil(item/k)
            if total <= H:
                return k
            k += 1