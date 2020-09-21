from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        min_heap = []
        heappush(min_heap, (matrix[0][0], 0, 0))
        count = 0
        n = len(matrix)
        val = None
        self.visited = set()
        while count < k:
            val, row, col = heappop(min_heap)
            self.push(row, col + 1, min_heap, n, matrix)
            self.push(row + 1, col, min_heap, n, matrix)
            count += 1
        return val

    def push(self, row, col, min_heap, n, matrix):
        if self.check_valid(row, col, n):
            heappush(min_heap, (matrix[row][col], row, col))
            self.visited.add((row, col))

    def check_valid(self, row, col, n):
        return row < n and col < n and (row, col) not in self.visited