from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = PriorityQueue()
        for i, (p0, p1) in enumerate(points):
            dist = (p0 ** 2 + p1 ** 2) ** (1 / 2)
            q.put((dist, (p0, p1)))

        ans = []
        for j in range(0, k):
            (_, point) = q.get()
            ans.append(point)

        return ans