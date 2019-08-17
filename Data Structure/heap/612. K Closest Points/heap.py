from heapq import heappush, heappop

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    # O(nlogk)
    def kClosest(self, points, origin, k):
        # write your code here
        min_heap = []
        result = []
        for i, point in enumerate(points):
            distance = (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
            heappush(min_heap, (-distance, -point.x, - point.y))
            if (len(min_heap) > k):
                heappop(min_heap)

        for i in range(k):
            distance, x, y = heappop(min_heap)
            result.append(Point(-x, -y))

        result.reverse()
        return result