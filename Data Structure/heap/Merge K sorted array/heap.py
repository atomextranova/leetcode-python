import heapq
from heapq import heappush, heappop


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # write your code here
        min_heap = []
        result = []

        for i in range(len(arrays)):
            if len(arrays[i]) == 0:
                continue
            heappush(min_heap, (arrays[i][0], i, 0))

        while len(min_heap) > 0:
            item, array_index, index = heappop(min_heap)
            result.append(item)
            if index + 1 < len(arrays[array_index]):
                heappush(min_heap, (arrays[array_index][index + 1], array_index, index + 1))

        return result