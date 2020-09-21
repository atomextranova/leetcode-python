import collections

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    """
    @param side_length: the length of a side of the lake (it's a square)
    @param lake_grid: a 2D matrix representing the lake 0= ice, 1= snowbank, -1= hole
    @param albert_row: row of Albert's snowbank
    @param albert_column: column of Albert's snowbank
    @param kuna_row: row of Kuna's snowbank
    @param kuna_column: column of Kuna's snowbank
    @return: a bool - whether Albert can escape
    """

    def lakeEscape(self, side_length, lake_grid, albert_row, albert_column,
                   kuna_row, kuna_column):
        # write your code here

        visited = {}
        visited[(albert_row, albert_column)] = [[0, 0, 0, 0], False]
        deque = collections.deque([(albert_row, albert_column)])

        while deque:
            x, y = deque.popleft()
            if x == kuna_row and y == kuna_column:
                visited[(x, y)][1] = True

            for i in range(4):
                if (x, y) in visited:
                    if visited[(x, y)][0][i] == -1:
                        continue
                    if visited[(x, y)][1] and visited[(x, y)][0][
                        i] == 2:
                        continue
                    if not visited[(x, y)][1] and visited[(x, y)][0][i] == 1:
                        continue
                    if visited[(x, y)][1] and visited[(x, y)][0][i] == 3:
                        return True
                dx, dy = DIR[i]
                new_x, new_y = x + dx, y + dy
                valid = self.is_valid(side_length, new_x, new_y)
                while valid:
                    if lake_grid[new_x][new_y] == 0:
                        new_x, new_y = new_x + dx, new_y + dy
                        valid = self.is_valid(side_length, new_x, new_y)
                        continue
                    elif lake_grid[new_x][new_y] == 1:
                        if (new_x, new_y) not in visited:
                            visited[(new_x, new_y)] = [[0, 0, 0, 0], visited[(x, y)][1]]
                        visited[(x, y)][0][i] += 1
                        deque.append((new_x, new_y))
                        break
                    else:
                        visited[(x, y)][0][i] = -1
                        break
                if not valid:
                    if visited[(x, y)][1]:
                        return True
                    visited[(x, y)][0][i] = 3
        return False

    def is_valid(self, n, x, y):
        return -1 < x < n and -1 < y < n