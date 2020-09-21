from heapq import heappush, heappop


class Solution:
    # Create min_heap,
    # store -distance to keep the smallest distance in reverse order
    # pop if len(min_heap) > k
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == 0 or not points:
            return []

        min_heap = []

        for point in points:
            x, y = point
            dist = self.distance(x, y)
            heappush(min_heap, (-dist, x, y))
            if len(min_heap) > K:
                heappop(min_heap)

        result = []
        while min_heap:
            _, x, y = heappop(min_heap)
            result.append((x, y))

        return result[::-1]

    def distance(self, x, y):
        return x ** 2 + y ** 2