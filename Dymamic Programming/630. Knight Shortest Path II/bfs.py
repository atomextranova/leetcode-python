import sys
from collections import deque


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    # input: 2d grid array, 1 stands for barrier, 0 for normal
    # output: shortest distance
    # edge cases:
    # 1. grid empty
    # 2. grid 1*1

    # bfs
    # Optimization: use set to record visited point, ignore

    def shortestPath2(self, grid):

        # write your code here
        n = len(grid)
        m = len(grid[0])

        if n == 1 and m == 1:
            return 0

        dx_list = (-1, -2, 1, 2)
        dy_list = (2, 1, 2, 1)

        queue = deque([(0, 0)])
        distance = 0
        visited = set()

        while len(queue) != 0:
            length = len(queue)
            distance += 1
            # Could also use visited hash function to record distance
            # always pop from left so that minimum distance is guaranteed
            for i in range(length):
                cur_x, cur_y = queue.popleft()
                for dx, dy in zip(dx_list, dy_list):
                    new_x, new_y = cur_x + dx, cur_y + dy
                    if not self.in_grid(new_x, new_y, n, m):
                        continue
                    if grid[new_x][new_y] == 1:
                        continue
                    if (new_x, new_y) in visited:
                        continue
                    visited.add((new_x, new_y))
                    if new_x == n - 1 and new_y == m - 1:
                        return distance
                    queue.append((new_x, new_y))

        return -1

    def in_grid(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m

