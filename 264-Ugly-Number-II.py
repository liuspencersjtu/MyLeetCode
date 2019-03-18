
import heapq
class Solution(object):
    def nthUglyNumber(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        if n == 1:
            return 1
        res = 1
        while n>1:
            p = heapq.heappop(heap)
            while heap and p == heap[0]:
                p = heapq.heappop(heap)
            a,b,c= 2*p,3*p,5*p
            heapq.heappush(heap,a)
            heapq.heappush(heap,b)
            heapq.heappush(heap,c)
            ###
            n-=1
            res = heap[0]
        return res
