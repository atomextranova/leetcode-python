DX = (-1, +1, 0, 0)
DY = (0, 0, -1, +1)

from collections import deque


class Solution:
    # Initialize count and fathers
    # count initialized to count of "1"s
    # for each position:
    # if not already visited (set or change to "0" after visited)
    # and == "1"
    # change it to visited
    # union its neighbors, count-- if union happens
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()
        row_len = len(grid)
        col_len = len(grid[0])
        self.count = 0
        fathers = [[(0, 0)] * col_len for _ in range(row_len)]
        for i in range(row_len):
            for j in range(col_len):
                fathers[i][j] = (i, j)
                if grid[i][j] == "1":
                    self.count += 1

        for i in range(row_len):
            for j in range(col_len):
                cell = grid[i][j]
                if cell == "0":
                    continue
                # grid[i][j] = "0"
                visited.add((i, j))
                for dx, dy in zip(DX, DY):
                    new_x = i + dx
                    new_y = j + dy
                    if self.check_index(new_x, new_y, row_len, col_len,
                                        visited):
                        if grid[new_x][new_y] == "1":
                            self.union(new_x, new_y, i, j, fathers)

        return self.count

    def find(self, x, y, fathers):
        if fathers[x][y] != (x, y):
            nx, ny = fathers[x][y]
            fathers[x][y] = self.find(nx, ny, fathers)
        return fathers[x][y]

    def union(self, x, y, x_2, y_2, fathers):
        root = self.find(x, y, fathers)
        root_2 = self.find(x_2, y_2, fathers)
        if root != root_2:
            fathers[root[0]][root[1]] = root_2
            self.count -= 1

    def check_index(self, x, y, row_len, col_len, visited):
        return 0 <= x < row_len and 0 <= y < col_len and (x, y) and (
        x, y) not in visited


sol = Solution()
print(sol.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
                      ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
