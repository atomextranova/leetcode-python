import heapq
from heapq import heappush, heappop


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # write your code here
        return self.merge_arrays(arrays, 0, len(arrays) - 1)

    def merge_arrays(self, arrays, start, end):
        if start == end:
            return arrays[start]

        mid = (start + end) // 2
        left = self.merge_arrays(arrays, start, mid)
        right = self.merge_arrays(arrays, mid + 1, end)

        return self.merge_array(left, right)

    def merge_array(self, array1, array2):
        result = []
        i, j = 0, 0
        while i < len(array1) and j < len(array2):
            element1 = array1[i]
            element2 = array2[j]
            if element1 < element2:
                result.append(element1)
                i += 1
            else:
                result.append(element2)
                j += 1

        while i < len(array1):
            element1 = array1[i]
            result.append(element1)
            i += 1

        while j < len(array2):
            element2 = array2[j]
            result.append(element2)
            j += 1

        return result