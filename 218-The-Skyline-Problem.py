class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        idx, n = 0, len(buildings)
        # use heap to keep track of the current height
        liveBuildings, skyline = [], []
        # 先进堆记录最高楼， 出堆标记skyline
        while idx<n or len(liveBuildings) > 0:
            if len(liveBuildings) == 0 or (idx<n and buildings[idx][0] <= -liveBuildings[0][1]):
                start = buildings[idx][0]
                while idx < n and buildings[idx][0] == start:
                    # maxheap: [height, end_of_building]
                    heapq.heappush(liveBuildings, [-buildings[idx][2], -buildings[idx][1]])
                    idx += 1
            else:
                start = -liveBuildings[0][1]
                # while to in case multiple buildings start at the same address
                # pop end的时候把当前最低的高度加入skyline
                while len(liveBuildings) > 0 and -liveBuildings[0][1] <=  start:
                    heapq.heappop(liveBuildings)
            height = len(liveBuildings) and -liveBuildings[0][0]
            if len(skyline) == 0 or skyline[-1][-1] != height:
                skyline.append([start, height])
        return skyline
        
