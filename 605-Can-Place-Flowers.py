class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        preNzero = 1
        ones = n
        flowerbed.append(0)
        if ones==0:
            return True
        for i in flowerbed:
            if not i and preNzero>=2:
                ones-=1
                preNzero=0
                if ones==0:
                    return True
            if i:
                preNzero=0
            else:
                preNzero+=1
        return False
                