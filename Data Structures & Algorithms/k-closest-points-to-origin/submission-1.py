class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        res = []
        for point in points:
            d = (point[0])**2 + (point[1])**2
            heapq.heappush(res, (-d, point))

            if len(res) > k:
                heapq.heappop(res)
        return [point for d, point in res]
        