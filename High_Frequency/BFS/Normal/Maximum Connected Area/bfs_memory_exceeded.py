import collections

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    """
    @param matrix: the matrix for calculation.
    @return: return the max area after operation at most once.
    """

    def maxArea(self, matrix):
        # write your code here.
        if not matrix:
            return 0

        visited = set()
        row_len = len(matrix)
        col_len = len(matrix[0])
        areas = [[0] * col_len for _ in range(row_len)]
        max_area = 0
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    continue

                deque = collections.deque([(i, j)])
                visited.add((i, j))
                cur_size = 1
                cur_area = [(i, j)]
                while deque:
                    x, y = deque.popleft()
                    for dx, dy in DIR:
                        new_x, new_y = x + dx, y + dy
                        if not self.is_valid(row_len, col_len, new_x, new_y):
                            continue

                        deque.append((new_x, new_y))
                        cur_area.append((new_x, new_y))
                        visited.add((new_x, new_y))
                        cur_size += 1

                for x, y in cur_area:
                    areas[x][y] = cur_size
        for x in range(row_len):
            for y in range(col_len):
                if matrix[x][y] == 1:
                    continue
                cur_size = 1
                for dx, dy in DIR:
                    new_x, new_y = x + dx, y + dy
                    if not self.is_valid(row_len, col_len, new_x, new_y):
                        continue
                    cur_size += areas[new_x][new_y]
                max_area = max(max_area, cur_size)

        return max_area

    def is_valid(self, row_len, col_len, x, y):
        return -1 < x < row_len and -1 < y < col_len
