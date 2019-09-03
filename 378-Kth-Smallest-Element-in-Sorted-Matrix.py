import heapq
class Solution:
    # This solution only use the sorted trait of the row, not column
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        heap = [(row.pop(0), idx) for idx, row in enumerate(matrix)]
        while True:
            heapq.heapify(heap)
            it, idx = heapq.heappop(heap)
            k-=1
            if k==0:
                return it
            else:
                try:
                    heapq.heappush(heap,(matrix[idx].pop(0),idx))
                except:
                    pass
