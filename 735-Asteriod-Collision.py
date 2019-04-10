class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        res = []
        for it in asteroids:
            if it<0:
                while res and res[-1]>0 and res[-1]<(-it):
                    res.pop()
                if not res or res[-1]<0:
                    res.append(it)
                elif res[-1] == (-it):
                    res.pop()
            else:
                res.append(it)
        return res
