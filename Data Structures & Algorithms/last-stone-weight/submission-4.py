import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while heap:
            if not stones:
                return 0
            if heap and len(heap) == 1:
                return -heap[0]
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 == stone2:
                continue
            else:
                smash = stone1 - stone2
                heapq.heappush(heap, -smash)
        return 0
