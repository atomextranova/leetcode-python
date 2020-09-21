class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []

        row = len(matrix)
        col = len(matrix[0])
        n = row * col
        result = [0] * n

        diffs = [(-1, 1), (1, -1)]
        direct = 0

        x, y = 0, 0
        for i in range(n):
            result[i] = matrix[x][y]

            x += diffs[direct][0]
            y += diffs[direct][1]

            if x >= row:
                x -= 1
                y += 2
                direct = (direct + 1) % 2
            if y >= col:
                y -= 1
                x += 2
                direct = (direct + 1) % 2
            if x < 0:
                x += 1
                direct = (direct + 1) % 2
            if y < 0:
                y += 1
                direct = (direct + 1) % 2

        return result