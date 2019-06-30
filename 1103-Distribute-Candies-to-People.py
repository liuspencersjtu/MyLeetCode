import math
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        #x(x+1)<candies*2<(x+1)^2
        cnt = math.floor(math.sqrt(2*candies))
        if cnt*(cnt+1)>=2*candies:
            cnt-=1
        res = [0]*num_people
        for i in range(1, cnt+1):
            res[i%num_people-1] += i
        #print(cnt)
        res[i%num_people] += candies - cnt*(cnt+1)//2
        return res
