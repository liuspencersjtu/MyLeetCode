class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        if start >destination:
            start, destination = destination, start
        tmp = sum(distance[start:destination])
        return min(tmp, total - tmp)
