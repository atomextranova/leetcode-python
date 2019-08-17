import sys


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    # State: dp_table[x][y]: the shortest distance to point (x, y) on board
    # Function: dp_table[x][y] = min(dp_table[x - dx][y - dy] + 1) where
    # dx, dy are specified in the question, if reachable
    # e.g. in grid and not barrier
    # Initialization: dp_table[0][0] = 0, others also = sys.maxsize
    # Answer: dp_table[n-1][m-1] if reachable, or -1

    # Optimization: at most need to keep 2 lines of history and 1 line of result
    # because max(dy) = 2
    # Need to reinitialize the next line to update to sys.maxsize after every dp
    # update

    def shortestPath2(self, grid):
        # write your code here
        n = len(grid)
        m = len(grid[0])

        dp_table = [[sys.maxsize] * 3 for _ in range(n)]
        dp_table[0][0] = 0

        dx_list = (-1, -2, 1, 2)
        dy_list = (2, 1, 2, 1)
        for y in range(m):
            if y > 0:
                for x in range(n):
                    dp_table[x][y % 3] = sys.maxsize
            for x in range(n):
                if grid[x][y] == 1:
                    continue
                for dx, dy in zip(dx_list, dy_list):
                    old_x = x - dx
                    old_y = y - dy
                    if not self.in_grid(old_x, old_y, n, m):
                        continue
                    dp_table[x][y % 3] = min(dp_table[old_x][old_y % 3] + 1,
                                             dp_table[x][y % 3])

        if dp_table[n - 1][(m - 1) % 3] == sys.maxsize:
            return -1

        return dp_table[n - 1][(m - 1) % 3]

    def in_grid(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m

