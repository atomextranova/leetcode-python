from heapq import heappush, heappop


class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """

    # Edge case:
    # 1. Matrix empty
    # 2. k < 1, k > size(matrix)

    # Heap
    # O*(klogn*) time, n is the maximum of the width and height of the matrix.

    # Key: visited to avoid duplicates
    def kthSmallest(self, matrix, k):
        # write your code here
        min_heap = [(matrix[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        count = 0
        length_x, length_y = len(matrix), len(matrix[0])
        while count < k - 1:
            count += 1
            element, x, y = heappop(min_heap)

            new_x = x + 1
            new_y = y
            if self.in_matrix(new_x, new_y, length_x, length_y) \
                    and (new_x, new_y) not in visited:
                down_element = matrix[new_x][new_y]
                heappush(min_heap, (down_element, new_x, new_y))
                visited.add((new_x, new_y))
            new_x = x
            new_y = y + 1
            if self.in_matrix(new_x, new_y, length_x, length_y) \
                    and (new_x, new_y) not in visited:
                right_element = matrix[new_x][new_y]
                heappush(min_heap, (right_element, new_x, new_y))
                visited.add((new_x, new_y))

        element, _, _ = heappop(min_heap)
        return element

    def in_matrix(self, x, y, length_x, length_y):
        return x < length_x and y < length_y