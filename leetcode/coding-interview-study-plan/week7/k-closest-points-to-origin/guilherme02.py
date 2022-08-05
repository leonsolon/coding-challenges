import heapq
from math import pow


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = pow(x, 2) + pow(y, 2)
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(0, k):
            dist, x, y = heapq.heappop(heap)
            result.append([x,y])

        return result